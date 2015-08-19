#!/usr/bin/env python

from __future__ import print_function

import argparse

def hello():
    """ Says hello """

    parser = argparse.ArgumentParser()
    parser.add_argument('name', help="name of person to greet")
    parser.add_argument('-r', '--repeat', type=int, default=1,
            help="number of times to print the greeting")
    args = parser.parse_args()

    for i in xrange(args.repeat):
        print("Hello, {0}!".format(args.name))

if __name__ == '__main__':
    hello()
