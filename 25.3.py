# 680 kompege

for val in range(485617, 529678 + 1):
    v = val
    div = 2
    divs = []
    f = False
    while div*div <= v:
        if v % div == 0:
            divs += [div]
            v //= div
            if v % div == 0:
                f = True
                break
        div += 1
    
    if f:
        continue
    divs += [v]
    if len(divs) == 3 and divs[2] - divs[0] < 100 and len(set(v%10 for v in divs)) == 1:
        print(val, divs[2] - divs[0])
