# 18 kompege
from functools import lru_cache
def move(a, b):
    return [solve(a, b) for a, b in [(a + 1, b), (a, b + 1), (a*2, b), (a, b*2)]]

@lru_cache(None)
def solve(a, b):
    if a + b >= 77:
        return -0

    mas = move(a, b)

    if all(v > 0 for v in mas):
        return -max(mas)
    else:
        return -max(v for v in mas if v <= 0) + 1

for s in range(1, 70):
    if solve(7, s) == +2:
        print(s)

print('-------------')

for s in range(1, 70):
    if solve(7, s) == -2:
        print(s)
