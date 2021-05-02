from enum import IntEnum, auto
import sys


class _(IntEnum):
    C = 0
    Db = auto()
    D = auto()
    Eb = auto()
    E = auto()
    F = auto()
    Gb = auto()
    G = auto()
    Ab = auto()
    A = auto()
    Bb = auto()
    B = auto()

    def __repr__(self):
        return self.name

    def __add__(self, other):
        return _((self.value + other.value) % 12)

    def __sub__(self, other):
        return _((self.value - other.value) % 12)


scales = {
    'major': {_.C, _.D, _.E, _.F, _.G, _.A, _.B},
    'minor': {_.C, _.D, _.Eb, _.F, _.G, _.Ab, _.Bb},
}


def transpose(xs, root):
    return {x + root for x in xs}


def get_score(xs, ys):
    intersection = xs & ys
    score = len(intersection)
    return score


if __name__ == "__main__":
    root = sys.argv[1].upper()
    scale = sys.argv[2].lower()
    xs = transpose(scales[scale], _[root])
    results = []
    for root in _:
        for name, scale in scales.items():
            ys = transpose(scale, root)
            score = get_score(xs, ys)
            results.append((score, root, name, ys))

    for x in sorted(results, key=lambda x: x[0], reverse=True):
        print(x)
