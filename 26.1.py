# 24 kompege

f = open(r"D:\Downloads\26 (9).txt")

S, N = map(int, f.readline().split())

mas = []

for line in f:
    mas += [int(line)]

mas.sort()

s = 0
n = 0

while s + mas[n] <= S:
    s += mas[n]
    n += 1

print(n)
n -= 1
s -= mas[n]
while mas[n+1] <= S - s:
    n += 1
print(mas[n])
