"""CLI entrypoint for chataction."""

from __future__ import annotations

from collections.abc import Iterable

import click

from chataction import __version__

ROOT_SUMMARY = "ChatAction action orchestration CLI."


def _purpose(command: click.Command) -> str:
    """Return a compact one-line purpose for a Click command."""

    text = command.short_help or command.help or "Run this command."
    return " ".join(text.strip().split()).rstrip(".") + "."


def _option_signature(command: click.Command) -> str:
    """Render a compact signature for visible command params."""

    parts: list[str] = []
    for param in command.params:
        if getattr(param, "hidden", False):
            continue
        if isinstance(param, click.Argument):
            name = param.name.replace("_", "-").upper()
            marker = f"<{name}>"
            if not param.required:
                marker = f"[{marker}]"
            parts.append(marker)
            continue
        if isinstance(param, click.Option):
            visible_opts = [opt for opt in param.opts if opt.startswith("--")] or list(param.opts)
            if not visible_opts:
                continue
            opt = visible_opts[0]
            if param.is_flag:
                parts.append(f"[{opt}]")
            else:
                metavar = (param.metavar or param.name or "VALUE").replace("_", "-").upper()
                parts.append(f"[{opt} <{metavar}>]")
    return " ".join(parts)


def _visible_commands(group: click.Group) -> Iterable[tuple[str, click.Command]]:
    for name in sorted(group.commands):
        command = group.commands[name]
        if getattr(command, "hidden", False):
            continue
        yield name, command


def _render_command(name: str, command: click.Command, prefix: str, is_last: bool) -> list[str]:
    connector = "└── " if is_last else "├── "
    child_prefix = prefix + ("    " if is_last else "│   ")
    signature = _option_signature(command)
    display = name if not signature else f"{name} {signature}"
    lines = [f"{prefix}{connector}{display}  # {_purpose(command)}"]

    if isinstance(command, click.Group):
        children = list(_visible_commands(command))
        for index, (child_name, child_command) in enumerate(children):
            lines.extend(_render_command(child_name, child_command, child_prefix, index == len(children) - 1))
    return lines


def render_cli_tree(command: click.Group, *, root_name: str = "chataction") -> str:
    """Render the registered Click command tree for ChatAction."""

    entries: list[tuple[str, str | click.Command]] = [
        ("--help", "Show this help message."),
        ("--version", "Show the installed package version."),
        ("--tree", "Print the registered command tree."),
    ]
    entries.extend(_visible_commands(command))

    lines = [f"{root_name}  # {ROOT_SUMMARY}"]
    for index, (name, value) in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        if isinstance(value, click.Command):
            lines.extend(_render_command(name, value, "", is_last))
        else:
            lines.append(f"{connector}{name}  # {value}")
    return "\n".join(lines)


def _print_tree(ctx: click.Context, _param: click.Parameter, value: bool) -> None:
    if not value or ctx.resilient_parsing:
        return
    command = ctx.command
    if not isinstance(command, click.Group):
        raise click.ClickException("Command tree is only available for command groups.")
    click.echo(render_cli_tree(command, root_name=ctx.info_name or "chataction"))
    ctx.exit()


@click.group(name="chataction", context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__, prog_name="chataction")
@click.option(
    "--tree",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    callback=_print_tree,
    help="Print the registered command tree and exit.",
)
def main() -> None:
    """ChatAction command line interface."""


if __name__ == "__main__":
    main()
