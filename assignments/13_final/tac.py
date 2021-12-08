#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-12-07
Purpose: Print lines in reverse
"""


import argparse
import sys


# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('infile',
                        nargs='+',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt', encoding='UTF-8'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt', encoding='UTF-8'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------

def main():
    """Make a jazz noise here"""

    args = get_args()

    for file in args.infile:
        llist = [line.rstrip() for line in file]
        llist.reverse()
        for item in llist:
            print(item, file=args.outfile)

# --------------------------------------------------


if __name__ == '__main__':
    main()
