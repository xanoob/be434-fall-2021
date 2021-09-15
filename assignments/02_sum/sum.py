#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-09-14
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('int',
                        metavar='INT',
                        nargs='+',
                        type=int,
                        help='Numbers to add')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_addends = len(args.int)
    sum_all = sum(args.int)

    if num_addends == 1:
        addends = args.int[0]

    else:
        addends = [str(i) for i in args.int]
        addends = ' + '.join(addends)

    print(addends, "=", sum_all)



# --------------------------------------------------
if __name__ == '__main__':
    main()
