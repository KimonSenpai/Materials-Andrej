
def f(s):
    while s.find('111') != -1:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)

    return s

i = 31
while f('1'*i) != '211':
    i += 1
print(i)