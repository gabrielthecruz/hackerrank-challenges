from collections import deque
from sys import stdin


def can_be_piled(sides):
    cubes = deque(sides)
    last = None

    while cubes:
        if cubes[0] >= cubes[-1]:
            cube = cubes.popleft()
        else:
            cube = cubes.pop()

        if last is not None and last < cube:
            return False

        last = cube

    return True


def piling_up():
    _, *tests = stdin.readlines()

    for sides in tests[1::2]:
        if can_be_piled(int(cs) for cs in sides.split()):
            print('Yes')
            continue

        print('No')


if __name__ == '__main__':
    piling_up()
