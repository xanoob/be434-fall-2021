#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-09-13
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to store items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    itemcount = len(args.items)

    if args.sorted:
        items.sort()

    thingbring = ''

    if itemcount == 1:
        thingbring = items[0]

    elif itemcount == 2:
        thingbring = ' and '.join(items)

    else:
        items[-1] = 'and ' + items[-1]
        thingbring = ', '.join(items)

    print("You are bringing " + thingbring + ".")

# --------------------------------------------------
if __name__ == '__main__':
    main()
