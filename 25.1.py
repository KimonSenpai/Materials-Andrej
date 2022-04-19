# 67 kompege

# x = a * b
# x = y * y
# x = 2^p * 3^q * 5^r (3^y * 5^z)
for val in range(81234, 134689 + 1):
    div = 2
    divs = []
    while div*div <= val:
        if val % div == 0:
            divs += [div]
            if div*div != val:
                divs += [val//div]
        div += 1
    
    if len(divs) == 3:
        divs.sort()
        print(*divs)