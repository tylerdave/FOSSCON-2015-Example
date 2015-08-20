#!/usr/bin/env python

import click

@click.command()
@click.argument('name')
@click.option('--count', '-c', default=1,
        help="Number of times to print the greeting")
def hello(name, count):
    """ Click CLI to greet the provided NAME. """

    for i in xrange(count):
        print("Hello, {0}!".format(name))


if __name__ == '__main__':
    hello()
