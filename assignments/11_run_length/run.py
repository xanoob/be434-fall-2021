#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-11-16
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

    parser.add_argument('str',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.str):
        args.str = open(args.str, 'rt').read()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    test_ls = []
    for seq in args.str.splitlines():
        seq = seq + "." # indicate end of line
        prev = "none"
        count = 1
        for letter in seq:
            # print("current", letter)
            # print("previous", prev)
            if prev == "none": # start of line
                prev = letter
                # print("start", letter, count)
            elif letter == prev: # current letter same as previous
                count += 1
                # print("same", letter, count)
            elif letter == "." : # reached end of line
                # print(prev, count)
                test_ls.append([prev,count])
            else: # current letter different from previous
                test_ls.append([prev,count])
                prev = letter
                count = 1

    mainl = []
    for inl in test_ls:
        if inl[1] == 1:
            inl[1] = ''
        mainl.append(''.join(map(str, inl)))

    print(mainl)

    print(''.join(map(str, mainl)))
# --------------------------------------------------

def rle(seq):
    """ Create RLE """
    prev = str()
    count = 0

    for letter in seq:
        print("current", letter)
        print("previous", prev)
        if prev == "none": # start of line
            prev = letter
            # print("start", letter, count)
        elif letter == prev: # current letter same as previous
            count += 1
            # print("same", letter, count)
        else: # current letter different than previous
            print("new letter", letter, count)
            prev = letter
            count = 1

# --------------------------------------------------
if __name__ == '__main__':
    main()
