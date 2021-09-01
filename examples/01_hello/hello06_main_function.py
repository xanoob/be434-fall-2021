#!/usr/bin/env python3
# Purpose: Say hello

import argparse

def main():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    args = parser.parse_args()
    print('Hello, ' + args.name + '!')

if __name__ == '__main__': # '__name__' is namespace, not related to function name.
    # name is where program starts. this is needed when you start using your code as a module and import into another python program
    main()
