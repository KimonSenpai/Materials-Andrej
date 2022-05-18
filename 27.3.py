# 23 kompege

for file in (r"D:\Downloads\27-A (7).txt", r"D:\Downloads\27-B (7).txt"):
    with open(file) as f:

        n = f.readline()

        S = 0
        diff = 10**6

        for line in f:
            a, b = map(int, line.split())

            S += max(a, b)
            if (a - b) % 3 != 0:
                diff = min(diff, abs(a - b))

        if S % 3 == 0:
            S -= diff
        print(S)