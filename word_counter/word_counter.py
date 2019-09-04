from collections import defaultdict
from sys import stdin


def word_counter(words):
    counter = defaultdict(int)

    for word in words:
        word = word.replace('\n', '')
        counter[word] += 1

    return counter


if __name__ == '__main__':
    _, *words = stdin.readlines()
    count = word_counter(words)
    print(len(count))
    print(*count.values())
