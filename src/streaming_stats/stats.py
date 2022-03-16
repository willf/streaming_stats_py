"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = streaming_stats.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This skeleton file can be safely removed if not needed!

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import sys
import streaming_stats
import json

from streaming_stats import __version__

__author__ = "Will Fitzgerald"
__copyright__ = "Will Fitzgerald"
__license__ = "MIT"

# > ping 8.8.8.8 | ack -oh '\d+\.\d{2,}' --flush  | python src/streaming_stats/cli.py

# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from streaming_stats.skeleton import fib`,
# when using this Python module as a library.



# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Streaming Stats")
    parser.add_argument(
        "--version",
        action="version",
        version="streaming_stats {ver}".format(ver=__version__),
    )
    parser.add_argument(
        "--every",
        "-n",
        dest="every",
        help="Print stats every nth value",
        type=int,
        default=0,
    )
    return parser.parse_args(args)



def main(args = sys.argv[1:]):
    args = parse_args(args)
    stats = streaming_stats.StreamingStats()
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            value = float(line)
            stats.append(value)
            if args.every and args.every > 0 and stats.n % args.every == 0:
                print(json.dumps(stats.dict()))
                sys.stdout.flush()
    print(json.dumps(stats.dict()))
    sys.stdout.flush()



if __name__ == "__main__":
    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m streaming_stats.cli 42
    #
    main()
