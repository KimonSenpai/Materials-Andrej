# ДЕЛ(A, 40) ∧ (ДЕЛ(780, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(180, x)))

def impl(a, b):
    return not a or b

def f(x, A):
    return (A%40 == 0 and (impl(780 % x == 0, impl(A%x != 0, 180 % x != 0))))

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)
        break