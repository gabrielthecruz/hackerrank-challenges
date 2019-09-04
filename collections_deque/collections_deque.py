from collections import deque
from sys import stdin


def main():
    _, *operations = stdin.readlines()
    d = deque()
    methods = {
        'append': d.append,
        'pop': d.pop,
        'popleft': d.popleft,
        'appendleft': d.appendleft
    }

    for operation in operations:
        name, *params = operation.replace('\n', '').split()

        if len(params) > 0:
            methods[name](*params)
        else:
            methods[name]()

    print(*list(d))


if __name__ == '__main__':
    main()
