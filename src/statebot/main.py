# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


import argparse
import logging
import sys

from statebot import __version__

__author__ = "Nick Syntychakis"
__copyright__ = "Nick Syntychakis"
__license__ = "Apache-2.0"

_logger = logging.getLogger(__name__)


def aws(args):
    # Implement aws logic here
    _logger.info(f"AWS Here: {args}")


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main():
    parser = argparse.ArgumentParser(prog="my_script", description="My Script")
    parser.add_argument(
        "--version",
        action="version",
        version=f"statebot {__version__}",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Create subparser for aws command
    parser_aws = subparsers.add_parser("aws", help="Run aws command")
    parser_aws.set_defaults(func=aws)

    args = parser.parse_args()
    setup_logging(args.loglevel)
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
