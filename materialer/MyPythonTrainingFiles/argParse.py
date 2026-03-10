#!/usr/bin/env python3
"""
A helper script demonstrating the use of Python's argparse module for building CLIs.
This script includes examples of arguments, options, help messages, and subcommands.
"""

import argparse
import datetime
from pathlib import Path

def list_directory(path, long=False):
    """List the contents of a directory, optionally in long format."""
    target_dir = Path(path)
    if not target_dir.exists():
        raise FileNotFoundError(f"The directory '{path}' does not exist.")

    for entry in target_dir.iterdir():
        if long:
            size = entry.stat().st_size
            date = datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime("%b %d %H:%M:%S")
            print(f"{size:>6d} {date} {entry.name}")
        else:
            print(entry.name)

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        prog="dirhelper",
        description="List the content of a directory, with optional details.",
        epilog="Thanks for using %(prog)s! :)"
    )

    # Add arguments and options
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the target directory (default: current directory)"
    )
    parser.add_argument(
        "-l", "--long",
        action="store_true",
        help="Display detailed directory content"
    )

    # Parse the arguments
    args = parser.parse_args()

    try:
        list_directory(args.path, args.long)
    except FileNotFoundError as e:
        parser.error(str(e))

if __name__ == "__main__":
    main()
