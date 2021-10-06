#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        help='DNA or RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='A writable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # make codon table
    codon_table = {}
    for line in args.codons:
        # kvpair = line.split()
        # codon_table[kvpair[0]] = kvpair[1]
        codon, letter = line.split()
        codon_table[codon] = letter

    # read codons
    k = 3
    seq = args.seq
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        print(codon_table.get(codon.upper(), "-"), end='', file=args.outfile)

    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
