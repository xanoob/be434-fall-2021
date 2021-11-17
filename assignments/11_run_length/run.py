#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-11-16
Purpose: Run Length Encoding of sequences in a line
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.str):
        with open(args.str, 'rt', encoding='utf-8') as in_f:
            args.str = in_f.read()

    return args

# --------------------------------------------------


def main():
    """Print RLE sequences"""

    args = get_args()

    for seq in args.str.splitlines():
        rle(seq)
        # rle_printer(line_ls)


# --------------------------------------------------


def rle(seq):
    """ for each line generate letter, value RLE pair """

    line_ls = []
    seq = seq + "."  # indicate end of line
    prev = "none"
    count = 1
    for letter in seq:
        if prev == "none":  # start of line
            prev = letter
        elif letter == prev:  # current letter same as previous
            count += 1
        elif letter == ".":  # reached end of line
            line_ls.append([prev, count])
        else:  # current letter different from previous
            line_ls.append([prev, count])
            prev = letter
            count = 1

    rle_printer(line_ls)


def rle_printer(line_ls):
    """take list of letter, count pairs from RLE and print"""

    pair_ls = []
    for pair in line_ls:
        if pair[1] == 1:
            pair[1] = ''
        pair_ls.append(''.join(map(str, pair)))
    print(''.join(map(str, pair_ls)))

# --------------------------------------------------


if __name__ == '__main__':
    main()
