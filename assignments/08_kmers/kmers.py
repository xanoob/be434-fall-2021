#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-10-26
Purpose: Find common k-mers between two files
"""

import argparse
import collections

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common k-mers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('FILE1',
                        help='Input file 1',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    args = parser.parse_args()

    if not args.kmer > 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args

# --------------------------------------------------


def main():
    """Print out table of k-mers and counts"""

    args = get_args()
    file1_ls = lines_to_list(args.FILE1)
    file2_ls = lines_to_list(args.FILE2)

    file1_kdict = get_kmer_freq(file1_ls, args.kmer)
    file2_kdict = get_kmer_freq(file2_ls, args.kmer)

    key_shared = list(set(file1_kdict.keys()).intersection(file2_kdict.keys()))

    for key in key_shared:
        print(f'{key:10}{file1_kdict.get(key):6}{file2_kdict.get(key):6}')

# --------------------------------------------------


def get_kmer_freq(inlist, k):
    """ Returns dictionary with frequency of k-mers given a list """

    kmer_list = [find_kmers(word, k) for word in inlist]

    return dict(collections.Counter(flatlist(kmer_list)))


def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


def flatlist(nested_list):
    """ flattens nested list """

    flat_list = [item for inner_list in nested_list for item in inner_list]
    return flat_list


def lines_to_list(infile):
    """ put all words in a file into a list """

    nested_list = [line.split() for line in infile]
    flat_list = flatlist(nested_list)
    return flat_list


# --------------------------------------------------


if __name__ == '__main__':
    main()
