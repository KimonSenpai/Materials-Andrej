# 7321 reshu-ege

n, t = map(int, input().split())
A = 0
B = t
for i in range(n):
    a, b = map(int, input().split())

    A += a
    B = min(B + b, A + t)

print(B)