#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-10-11
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='Vowel to replace',
                        metavar='str',
                        type=str,
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if args.vowel.lower not in 'aeiou':
        parser.error(f'--vowel "{args.vowel}" is not a vowel')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()




# --------------------------------------------------
if __name__ == '__main__':
    main()
