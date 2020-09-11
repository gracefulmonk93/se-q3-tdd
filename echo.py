#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Leann James with help from Joseph Hafed"


import sys
import argparse

# usage: echo.py [-h] [-u] [-l] [-t] text

# Perform transformation on input text.

# positional arguments:
#   text         text to be manipulated

# optional arguments:
#   -h, --help   show this help message and exit
#   -u, --upper  convert text to uppercase
#   -l, --lower  convert text to lowercase
#   -t, --title  convert text to titlecase


def create_parser():
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    text = ns.text
    if ns.upper:
        print(text.upper())
    elif ns.lower:
        print(text.lower())
    elif ns.title:
        print(text.title())
    else:
        print(text)


if __name__ == '__main__':
    main(sys.argv[1:])
