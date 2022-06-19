# 842 kompege
from functools import lru_cache
def go(a, b):
    mas = []

    if a > 0:
        mas += [solve(a - 1, b)]
    if b > 0:
        mas += [solve(a, b - 1)]
    if a > 1:
        mas += [solve(a//2 + a%2, b)]
    if b > 1:
        mas += [solve(a, b//2 + b%2)]

    return mas
@lru_cache(None)
def solve(a, b):
    if a + b <= 32:
        return -0
    
    mas = go(a, b)

    if all(v > 0 for v in mas):
        return -max(mas)
    else:
        return -max(v for v in mas if v <= 0) + 1


for s in range(23, 200):
    if solve(10, s) == -1:
        print(s)

print('---------------')

for s in range(23, 200):
    if solve(10, s) == +2:
        print(s)

print('---------------')

for s in range(23, 200):
    if solve(10, s) == -2:
        print(s)


