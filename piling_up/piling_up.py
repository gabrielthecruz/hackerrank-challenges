from collections import deque
from sys import stdin


class CubePile:
    def __init__(self, cubes, length=None):
        maxlen = len(cubes) if not length else length
        self.deque = deque(cubes, maxlen=maxlen)

    def __iter__(self):
        while self.deque:
            if self.deque[0] >= self.deque[-1]:
                yield self.deque.popleft()
            else:
                yield self.deque.pop()

    def can_be_piled(self):
        cubes = iter(self)
        last = next(cubes)

        for cube in cubes:
            if last < cube:
                return False

            last = cube

        return True


def piling_up():
    _, *tests = stdin.readlines()

    for n_cubes, n_sides in zip(tests[0::2], tests[1::2]):
        sides = (int(s) for s in n_sides.split())
        cubes_qty = int(n_cubes)
        pile = CubePile(sides, length=cubes_qty)

        if pile.can_be_piled():
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    piling_up()
