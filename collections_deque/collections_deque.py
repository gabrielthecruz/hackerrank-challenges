from collections import deque
from sys import stdin


def main():
    _, *operations = stdin.readlines()
    d = deque()
    methods = {key: getattr(d, key) for key in ['append', 'pop', 'popleft',
                                                'appendleft']}

    for operation in operations:
        name, *params = operation.strip().split()
        methods[name](*params)

    print(*d)


if __name__ == '__main__':
    main()
