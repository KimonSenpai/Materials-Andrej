# 1763 kompege

f = open(r"D:\Downloads\26 (11).txt")
N, M = map(int, f.readline().split())

mas = [int(line) for line in f]

sv = obr = 0

while sum(mas) >= M:
    mas.sort(reverse=True)
    m = M

    while mas[0] < m:
        m -= mas[0]
        sv += 1
        mas.pop(0)
    
    for i in range(0, len(mas) - 1):
        if mas[i + 1] < m:
            m -= mas[i]
            mas.pop(i)
            m = -m
            mas.insert(0, m)
            obr += m
            break

print(sv, obr)