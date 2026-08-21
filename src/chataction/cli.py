"""CLI entrypoint for chataction."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chataction import __version__


@click.group(name="chataction", context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__, prog_name="chataction")
@add_tree_option(renderer_options={"root_name": "chataction"})
def main() -> None:
    """ChatAction command line interface."""


if __name__ == "__main__":
    main()
