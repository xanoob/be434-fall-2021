#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-09-26
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file_in',
                        nargs='+',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-n',
                        '--number',
                        help='Option to print out line numbers',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_in = args.file_in

    for fh in file_in:
        for count, line in enumerate(fh, start=1):
            if args.number:
                print_format = "{:>6}\t{}"
                print(print_format.format(count, line.rstrip()))
            else:
                print(line.rstrip())

# --------------------------------------------------


if __name__ == '__main__':
    main()
