from __future__ import print_function

import argparse
import json
import logging
import sys
from pprint import pprint

try:
    from collections import Counter
except ImportError:
    from backport_collections import Counter


def get_char_counts(infile):
    text = infile.read()
    char_counter = Counter(text)
    return char_counter

def output_char_counts(char_counts, outfile):
    if outfile is sys.stdout:
        outfile.write(str(pprint(char_counts.most_common())))
    else:
        outfile.write(json.dumps(char_counts.most_common()))


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

    char_counts = get_char_counts(args.infile)
    output_char_counts(char_counts, args.outfile)

if __name__ == '__main__':
    cli()
