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
    'dorian': {_.C, _.D, _.Eb, _.F, _.G, _.A, _.Bb},
    'mixolydian': {_.C, _.D, _.E, _.F, _.G, _.A, _.Bb},
    'lydian': {_.C, _.D, _.E, _.Gb, _.G, _.A, _.B},
    'phrygian': {_.C, _.Db, _.Eb, _.F, _.G, _.Ab, _.Bb},
    'locrian': {_.C, _.Db, _.Eb, _.F, _.Gb, _.Ab, _.Bb},
    'whole_tone': {_.C, _.D, _.E, _.Gb, _.Ab, _.Bb},
    'half_whole_dim': {_.C, _.Db, _.Eb, _.E, _.Gb, _.G, _.A, _.Bb},
    'whole_half_dim': {_.C, _.D, _.Eb, _.F, _.Gb, _.Ab, _.A, _.B},
    'minor_blues': {_.C, _.Eb, _.F, _.Gb, _.G, _.Bb},
    'minor_pentatonic': {_.C, _.Eb, _.F, _.G, _.Bb},
    'major_pentatonic': {_.C, _.D, _.E, _.G, _.A},
    'harmonic_minor': {_.C, _.D, _.Eb, _.F, _.G, _.Ab, _.B},
    'harmonic_major': {_.C, _.D, _.E, _.F, _.G, _.Ab, _.B},
    'dorian_#4': {_.C, _.D, _.Eb, _.Gb, _.G, _.A, _.Bb},
    'phrygian_dominant': {_.C, _.Db, _.E, _.F, _.G, _.Ab, _.Bb},
    'melodic_minor': {_.C, _.D, _.Eb, _.F, _.G, _.A, _.B},
    'lydian_augmented': {_.C, _.D, _.E, _.Gb, _.Ab, _.A, _.B},
    'lydian_dominant': {_.C, _.D, _.E, _.Gb, _.G, _.A, _.Bb},
    'super_locrian': {_.C, _.Db, _.Eb, _.E, _.Gb, _.Ab, _.Bb},
    '8_tone_spanish': {_.C, _.Db, _.Eb, _.E, _.F, _.Gb, _.Ab, _.Bb},
    'bhairav': {_.C, _.Db, _.E, _.F, _.G, _.Ab, _.B},
    'hungarian_minor': {_.C, _.D, _.Eb, _.Gb, _.G, _.Ab, _.B},
    'hirajoshi': {_.C, _.D, _.Eb, _.G, _.Ab},
    'in_sen': {_.C, _.Db, _.F, _.G, _.Bb},
    'iwato': {_.C, _.Db, _.F, _.Gb, _.Bb},
    'kumoi': {_.C, _.D, _.Eb, _.G, _.A},
    'pelog_selisir': {_.C, _.Db, _.Eb, _.G, _.Ab},
    'pelog_tembung': {_.C, _.Db, _.F, _.G, _.Ab},
    'messiaen_3': {_.C, _.D, _.Eb, _.E, _.Gb, _.G, _.Ab, _.Bb, _.B},
    'messiaen_4': {_.C, _.Db, _.D, _.F, _.Gb, _.G, _.Ab, _.B},
    'messiaen_5': {_.C, _.Db, _.F, _.Gb, _.G, _.B},
    'messiaen_6': {_.C, _.D, _.E, _.F, _.Gb, _.Ab, _.Bb, _.B},
    'messiaen_7': {_.C, _.Db, _.D, _.Eb, _.F, _.Gb, _.G, _.Ab, _.A, _.B},
}


def transpose(xs, root):
    return {x + root for x in xs}


def get_score(xs, ys):
    intersection = xs & ys
    score_a = (len(intersection) * 2) / (len(xs) + len(ys))
    score_b = len(intersection) / len(xs)
    score_c = len(intersection) / len(ys)
    return max(score_a, score_b, score_c)


if __name__ == "__main__":
    root = sys.argv[1].upper()
    scale = sys.argv[2].lower()
    xs = transpose(scales[scale], _[root])
    results = []
    for root in _:
        for name, scale in scales.items():
            ys = transpose(scale, root)
            score = get_score(xs, ys)
            results.append((score, root, name, len(ys), ys))

    for res in sorted(results, key=lambda x: x[0], reverse=True):
        print('{:.3f}'.format(res[0]), res[1:])
