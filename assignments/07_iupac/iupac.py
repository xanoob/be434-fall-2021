#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-10-14
Purpose: Rock the Casbah
"""

import argparse
import sys
import re

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('SEQ',
                        metavar='SEQ',
                        nargs="+",
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Optional output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a pinniped noise here"""

    args = get_args()

    iupac = [('A', 'A'),
             ('C', 'C'),
             ('G', 'G'),
             ('T', 'T'),
             ('U', 'U'),
             ('R', '[AG]'),
             ('Y', '[CT]'),
             ('S', '[GC]'),
             ('W', '[AT]'),
             ('K', '[GT]'),
             ('M', '[AC]'),
             ('B', '[CGT]'),
             ('D', '[AGT]'),
             ('H', '[ACT]'),
             ('V', '[ACG]'),
             ('N', '[ACGT]')]

    for seq in args.SEQ:
        regex = str()
        for letter in seq:
            for value, pattern in iupac:
                if re.search(value, letter):
                    regex = regex + pattern
        print(seq, regex, file=args.outfile)

    if args.outfile != sys.stdout:
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
