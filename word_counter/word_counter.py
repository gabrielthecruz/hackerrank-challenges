from collections import Counter
from sys import stdin


def word_counter(words):
    counter = Counter(words)

    return len(counter), counter.values()


if __name__ == '__main__':
    _, *words = stdin.readlines()
    total, ns = word_counter(w.strip() for w in words)
    print(total)
    print(*ns)
