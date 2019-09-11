#!/bin/python3
import re

PATTERN = r'(?<=\w|\d)\W\D+?(?=\w|\d)'


def decode_matrix(matrix):
    string = ''.join(''.join(sp) for sp in zip(*matrix))

    return re.sub(PATTERN, ' ', string)


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


print(decode_matrix(matrix))
