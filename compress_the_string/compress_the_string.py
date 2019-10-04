from sys import stdin
from itertools import groupby


def compress_str(string):
    for char, group in groupby(string):
        length = len(list(group))

        print('({}, {})'.format(length, char), end=' ')


if __name__ == '__main__':
    string = stdin.read().strip()
    compress_str(string)
