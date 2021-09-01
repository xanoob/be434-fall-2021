#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
# if argument is optional (i.e flag) set a default value
parser.add_argument('-n', '--name', metavar='name',
                    default='World', help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')
