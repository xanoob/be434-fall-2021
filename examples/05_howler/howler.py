#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-09-26
Purpose: Rock the Casbah
"""

import argparse
import os
import sys



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, 'rt').read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    user_in = args.text.upper()

    fh_out = open(args.outfile, 'wt') if args.outfile else sys.stdout
    fh_out.write(user_in + '\n')
    fh_out.close()



# --------------------------------------------------
if __name__ == '__main__':
    main()
