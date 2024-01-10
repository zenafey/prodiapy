import argparse
import sys
import traceback
from typing import List, Optional

from prodiapy.cli.commands import login_parser


def construct_cli() -> argparse.ArgumentParser:
    base_parser = argparse.ArgumentParser(
        prog="prodiapy",
        description="Run Prodia API",
        add_help=True,
    )

    base_parser.add_argument(
        "-v",
        "--verbose",
        help="Verbose logging",
        action="store_true",
    )

    command_parser = base_parser.add_subparsers(dest="command")

    login_parser(command_parser)

    return base_parser


def execute_cli(
    parser: argparse.ArgumentParser,
    args: Optional[List[str]] = None,
) -> None:
    if args is None:
        args = sys.argv[1:]

    parsed_args = parser.parse_args(args=args)

    if (selected_func := getattr(parsed_args, "func", None)) is not None:
        selected_func(parsed_args)

    if parsed_args.command is None:
        parser.print_help()
        return


def _run() -> int:
    try:
        parser = construct_cli()
        execute_cli(parser)
    except Exception:
        traceback.print_exc()
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    _run()