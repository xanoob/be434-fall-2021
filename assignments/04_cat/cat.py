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
                        # nargs='+',
                        help='A readable file',
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
    print(type(file_in))
    lnum_flag = args.number

    for fh in file_in:
        # current_file = fh.readlines()
        for count, line in enumerate(fh, start=1):
            if lnum_flag:
                print_format = "{:>6}\t{}"
                # {:>6}\t{} right justified in field 6 chars wide
                print(print_format.format(count, line), end='')
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
