#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-11-22
Purpose: Find user-supplied patterns with re
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find patterns in a file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('PATTERN',
                        metavar='PATTERN',
                        type=str,
                        help='Search pattern')

    parser.add_argument('FILE',
                        help='Input file(s)',
                        nargs='+',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Get to grepping"""

    args = get_args()

    for infile in args.FILE:
        current_file_lines = infile.read().splitlines()
        for line in current_file_lines:
            if args.insensitive:
                result = re.findall(rf'{args.PATTERN}', line, re.I)
            else:
                result = re.findall(rf'{args.PATTERN}', line)
            if result:
                if len(args.FILE) > 1:
                    print(infile.name + ":" + line, file=args.outfile)
                else:
                    print(line, file=args.outfile)

# --------------------------------------------------


if __name__ == '__main__':
    main()
