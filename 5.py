# статград 2110201

#2021

def f(x):
    s = [0, 0]
    l = 0
    ch = 0
    while x > 0:
        d = x % 10
        if d % 2 == 0:
            ch += d
        
        s[l] += d
        l += 1
        x //= 10
    
    return abs(ch - s[l%2])

def g(x):
    x = str(x)
    ch = sum(int(d) for d in x if int(d)%2 == 0)
    if len(x) == 1:
        return ch
    else:
        return abs(ch - sum(int(d) for d in x[1::2]))

for i in range(2, 100000):
    if f(i) == 9:
        print(i)
        break