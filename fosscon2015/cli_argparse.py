from __future__ import print_function

import argparse
import json
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

    parser.add_argument('--verbose', '-v', action='store_true')

    args = parser.parse_args()


    if args.verbose:
        print("Command args: {0}".format(args), file=sys.stderr)

    text = args.infile.read()
    char_counts = Counter(text)

    print(json.dumps(dict(char_counts.most_common()), indent=2),
            file=args.outfile)


if __name__ == '__main__':
    cli()
