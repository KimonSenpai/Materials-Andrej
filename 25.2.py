# 2592 kompege


# x = 2^p * 3^q * 5^r (3^y * 5^z)
# count odd divs: (y + 1)*(z + 1)
# x = 2^p * q^4


def prime(x):
    div = 2
    while div*div <= x:
        if x % div == 0:
            return False
        div += 1

    return True


def In(x):
    return 55000000 <= x <= 60000000


q = 3
res = []
while q**4 <= 60000000:
    if not prime(q): 
        q += 1
        continue
    p = 0
    while 2**p * q**4 <= 60000000:
        if In(2**p * q**4):
            res += [(2**p * q**4, q**4)]
        p += 1
    q += 1
res.sort()
for v in res:
    print(*v)
