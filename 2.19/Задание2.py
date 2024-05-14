#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse


def list_files(startpath, max_depth=None, files_only=False, dirs_only=False, depth=0):
    if max_depth is not None and depth > max_depth:
        return

    for root, dirs, files in os.walk(startpath):
        if files_only:
            for filename in files:
                print(os.path.join(root, filename))
        elif dirs_only:
            for dirname in dirs:
                print(os.path.join(root, dirname))
        else:
            print(root)
            for filename in files:
                print(os.path.join(root, filename))
        if max_depth is not None and depth + 1 >= max_depth:
            break


def main():
    parser = argparse.ArgumentParser(description='Analog of tree utility in Linux')
    parser.add_argument('path', metavar='path', type=str, nargs='?', default='.',
                        help='Path to start tree view (default: current directory)')
    parser.add_argument('-d', '--max-depth', metavar='depth', type=int, help='Max depth to traverse')
    parser.add_argument('-f', '--files-only', action='store_true', help='Only display files')
    parser.add_argument('-r', '--dirs-only', action='store_true', help='Only display directories')

    args = parser.parse_args()

    list_files(args.path, args.max_depth, args.files_only, args.dirs_only)


if __name__ == '__main__':
    main()
