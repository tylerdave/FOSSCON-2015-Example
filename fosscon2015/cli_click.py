#!/usr/bin/env python

import click
import json
import sys

try:
    from collections import Counter
except ImportError:
    # backport_collections needed for python 2.6 compatibility
    from backport_collections import Counter


@click.command()
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
@click.option('--log-file', '-l', type=click.File('w'), default=sys.stderr)
@click.option('--verbose', '-v', is_flag=True)
def cli(infile, outfile, log_file, verbose):
    """ Count the occurances of characters in INFILE and output to OUTFILE. """

    if verbose:
        click.echo("Infile: {0}".format(infile), file=log_file)
        click.echo("Outfile: {0}".format(outfile), file=log_file)

    text = infile.read()
    char_counts = Counter(text)
    output = json.dumps(dict(char_counts.most_common()), indent=2)
    click.echo("Counted characters...", file=log_file)
    click.secho(output, file=outfile, fg='green')

    if verbose:
        click.echo("Done.".format(outfile), file=log_file)


if __name__ == '__main__':
    cli()
