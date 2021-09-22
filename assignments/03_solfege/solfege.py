#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-09-21
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('note',
                        metavar='str',
                        nargs='+',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------

def main():
    """Make a jazz noise here"""
    notes_dict = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread'}

    args = get_args()
    notes_list = args.note

    for item in notes_list:
        if item in notes_dict:
            itemc = item.capitalize()
            print(itemc + ", " + notes_dict.get(itemc), end='\n')
        else:
            print(f'I don\'t know "{item}"', end='\n')


# --------------------------------------------------


if __name__ == '__main__':
    main()
