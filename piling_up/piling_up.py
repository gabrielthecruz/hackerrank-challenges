from collections import deque
from sys import stdin


def pile_cubes(sides):
    stack = []

    while(sides):
        try:
            first, *sides, last = sides
            cubes = sorted([first, last], reverse=True)
        except ValueError:
            cubes = sides

        if len(stack) == 0 or any(stack[-1] >= c for c in cubes):
            stack += cubes
        else:
            return False

    return True


def get_cubes(input_cubes):
    cubes = deque(input_cubes)
    last_cube = None

    while cubes:
        right = cubes.pop()

        if len(cubes) > 0:
            left = cubes.popleft()

            if right >= left:
                biggest_cube = right
                cubes.appendleft(left)
            else:
                biggest_cube = left
                cubes.append(right)
        else:
            biggest_cube = right

        if last_cube is None or biggest_cube <= last_cube:
            last_cube = biggest_cube
        else:
            last_cube = None

        yield last_cube


def piling_up():
    _, *test_cases = stdin.readlines()

    for n_sides in test_cases[1::2]:
        sides = [int(s) for s in n_sides.split()]
        for cube in get_cubes(sides):
            if cube is None:
                print('No')
                break
        else:
            print('Yes')


if __name__ == '__main__':
    piling_up()
