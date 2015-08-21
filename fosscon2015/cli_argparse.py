from __future__ import print_function

import argparse
import json
import logging
import sys

try:
    from collections import Counter
except ImportError:
    # backport_collections needed for python 2.6 compatibility
    from backport_collections import Counter


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
            default=sys.stdin, help="Use - to read from stdin.")
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
            default=sys.stdout, help="Optional. By default, writes to stdout.")

    parser.add_argument('--log-file')
    parser.add_argument('--verbose', '-v', action='store_true')

    args = parser.parse_args()

    logger_args = {}
    if args.verbose:
        logger_args['level'] = logging.DEBUG
    if args.log_file:
        logger_args['filename'] = args.log_file

    logging.basicConfig(**logger_args)

    logging.debug("Command args: %s", args)

    text = args.infile.read()
    char_counts = Counter(text)

    args.outfile.write(json.dumps(dict(char_counts.most_common()), indent=2))


if __name__ == '__main__':
    cli()
