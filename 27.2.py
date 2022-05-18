# Найти максимальную сумму пары элементов, кратную 120.
# 7 = 2*3 + 1 (2 - целая часть от деления, 1 - остаток от деления)
# -7 = -2*3 - 1 = -3*3 + 2

f = open('')
n = f.readline()

mas = [-10**9]*120
max_sum = 0
for line in f:
    val = int(line)

    max_sum = max(max_sum, val + mas[-val%120])
    mas[val%120] = max(mas[val%120], val)
print(max_sum)