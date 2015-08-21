#!/usr/bin/env python

import click
import json

try:
    from collections import Counter
except ImportError:
    # backport_collections needed for python 2.6 compatibility
    from backport_collections import Counter


@click.command()
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
@click.option('--verbose', '-v')
def cli(infile, outfile, verbose):
    """ Count the occurances of characters in INFILE and save results in OUTFILE. """

    click.echo("Hi!")
    click.secho("infile: {0}".format(infile))
    click.secho("outfile: {0}".format(outfile))
    text = infile.read()
    char_counts = Counter(text)
    click.secho(json.dumps(dict(char_counts.most_common())), file=outfile,
            fg='green')


if __name__ == '__main__':
    cli()
