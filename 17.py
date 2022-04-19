# 37361 reshu-ege
f = open(r"D:\Downloads\17 (2).txt")

mas = list(map(int, f.readlines()))
n = len(mas)
cnt = 0
max_sum = -1
for i in range(n - 1):
    for j in range(i + 1, n):
        if (mas[i] + mas[j]) % 126 == 0:
            cnt += 1
            max_sum = max(max_sum, mas[i] + mas[j])
print(cnt, max_sum)
