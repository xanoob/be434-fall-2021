#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-09-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        type=str,
                        help='Input text')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    jumpcode = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0', '6':'4', '7':'3', '8':'2', '9':'1',
                '0':'5'}
    args = get_args()
    str_input = args.positional
    for char in str_input:
    #     if char in jumpcode:
    #         print(jumpcode[char], end='')
    #     else:
    #         print(char, end='')
        print(jumpcode.get(char,char),end='')



# --------------------------------------------------
if __name__ == '__main__':
    main()
