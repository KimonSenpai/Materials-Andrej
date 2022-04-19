
from functools import lru_cache

@lru_cache(None)
def f(fr, to):
    if to == fr:
        return 1
    if to < fr:
        return 0
    res = f(fr, to - 1) + f(fr, to - 2)
    if to % 2 == 0:
        res += f(fr, to//2)

    return res

print(f(4, 9)*f(9, 12)*f(12, 15))