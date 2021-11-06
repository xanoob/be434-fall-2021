#!/usr/bin/env python3
"""
Author : RoxanneB <RoxanneB@localhost>
Date   : 2021-11-03
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()

# --------------------------------------------------


def compare_pos(lines, num_lines, num_pos):
    """ compare each letter position in any number of lines """

    letter_match = {}
    for letter in range(num_pos):
        compare = [lines[line][letter] for line in range(num_lines)]
        if len(set(compare)) != 1:  # 1 if everything in set matches
            letter_match[letter] = 'X'
        else:
            letter_match[letter] = '|'

    return letter_match

# --------------------------------------------------


def main():
    """Run comparison and print"""

    args = get_args()

    line_list = [line.rstrip() for line in args.FILE]
    num_lines = len(line_list)
    num_pos = len(line_list[0])  # assuming all lines are equal length

    pos_match = compare_pos(line_list, num_lines, num_pos)

    for lines in line_list:
        print(lines.rstrip())

    for pos in range(num_pos):
        print(pos_match[pos], end='')


# --------------------------------------------------

if __name__ == '__main__':
    main()
