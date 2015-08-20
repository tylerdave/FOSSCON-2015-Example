#!/usr/bin/env python

from __future__ import print_function

import argparse

def hello():
    """ Argparse CLI to greet the provided NAME. """

    parser = argparse.ArgumentParser()
    parser.add_argument('name', help="name of person to greet")
    parser.add_argument('-c', '--count', type=int, default=1,
            help="number of times to print the greeting")
    args = parser.parse_args()

    for i in xrange(args.count):
        print("Hello, {0}!".format(args.name))

if __name__ == '__main__':
    hello()
