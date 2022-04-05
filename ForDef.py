

'''
for p in [1, 3, 4, 6]:
    print(p)

def my_range(a, b, s):
    i = a
    while i < b:
        yield i
        i += s

for i in my_range(3, 8, 2):
    print(i)


gen = my_range(3, 7, 2)

print('-----------------------')
print(next(gen))
print(next(gen))
#print(next(gen))

print("=======================")


def my_abs(val):
    if val >= 0:
        return val
    
    return -val

    #return -val + val**2 == 30


v = my_abs(3 - 5) + 7
'''
mas = [i**2 for i in range(9)]

#print(mas)
#print(*mas)

#mas = mas + [mas]*2
# [0, 1, 4, [0, 1, 4], [0, 1, 4]]
print(mas[:])
print(mas[::-1])
print(mas[3:6:2])

print(mas[-1:-4:-1])

print(sum(mas))
print(list(map(str, mas)))
print(list(zip(mas, mas[::-1])))
print(list(zip([1, 2, 3], [1, 2])))
def g(x):
    return x%2 == 0

print(list(filter(lambda x: x%2 == 0, mas)))



x = [1, 3, 4, 5, 8, 3]
y = [2, 4, 1, 5, 7, 3]

# s = sqrt(x[1]*y[1] + ... x[n]*y[n])

print(sum([X*Y for X, Y in zip(x, y)])**0.5)
print(list(range(1, 5)))