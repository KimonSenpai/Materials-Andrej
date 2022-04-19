from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if 2*n%3 == 0:
        return f(n-1) + f(2*n//3)
    else:
        return f(n - 1)

print(f(20))