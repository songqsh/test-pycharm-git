# my functions.py

def plus_two(n):
    out = n + 2
    return out


def fall_dist(t, g=9.81):
    d = 0.5 * g * t ** 2
    return d


def plus_four(n: int) -> int:
    return plus_two(plus_two(n))
