#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-10-07
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('infile1',
                        help='Input file 1',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('infile2',
                        help='Input file 2',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Optional output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------

def lines_to_list(infile):
    """ put all words in a file into a list """
    nested_list = [line.split() for line in infile]
    # nested_list = []
    # for line in infile:
    #     nested_list.append(line.split())
    flat_list = [item for inner_list in nested_list for item in inner_list]
    # flat_list = []
    # for inner_list in nested_list:
    #     for item in inner_list:
    #         flat_list.append(item)

    return flat_list


def main():
    """Make a jazz noise here"""

    args = get_args()
    infile1_ls = lines_to_list(args.infile1)
    infile2_ls = lines_to_list(args.infile2)

    file_intersect = sorted(list(set(infile1_ls).intersection(infile2_ls)))

    for word in file_intersect:
        print(word, file=args.outfile)

# --------------------------------------------------


if __name__ == '__main__':
    main()
