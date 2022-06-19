f = open("27_B.txt")

N = int(f.readline())

mas = []
for line in f:
    mas += [int(line)]

max_s, min_l = -10**19, 10**19
for i in range(0, N):
    for j in range(i, N + 1):
        s = sum(mas[i:j])
        if s % 27 != 0:
            if s > max_s:
                max_s = s
                min_l = j - i
            elif s == max_s:
                min_l = min(min_l, j - i)

print(min_l)
        