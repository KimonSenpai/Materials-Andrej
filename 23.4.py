from functools import lru_cache

@lru_cache(None)
def f(fr, to):
    if fr == to:
        return 1
    if fr > to or to == 30:
        return 0

    res = f(fr, to - 1)

    if to % 3 == 0:
        res += f(fr, to//3)
    if to % 4 == 0:
        res += f(fr, to//4)
    return res

print(f(2, 15)*f(15, 100))