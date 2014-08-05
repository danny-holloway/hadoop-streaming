#!/usr/bin/env python
from argparse import ArgumentParser
from csv import reader
import sys


def process(k, v, file):
    for parts in reader(file):
        try:
            key = parts[k].strip()
            value = parts[v].strip()
            print '%s\t%s' % (key, value)
        except:
            pass

if __name__ == '__main__':
    parser = ArgumentParser(description='Simple MapReduce mapper')
    parser.add_argument('key', type=int)
    parser.add_argument('value', type=int)
    args = parser.parse_args()
    process(args.key, args.value, sys.stdin)
