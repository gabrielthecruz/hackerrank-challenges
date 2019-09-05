from collections import Counter
from sys import stdin


def company_logo():
    company_name = stdin.readline().replace('\n', '')
    chars = Counter(sorted(company_name))

    for char in chars.most_common(3):
        print(*char)


if __name__ == '__main__':
    company_logo()
