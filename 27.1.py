# Последовательность натуральных чисел характеризуется 
# числом Х — наибольшим числом, кратным 14 и являющимся 
# произведением двух элементов последовательности с различными 
# номерами. Гарантируется, что хотя бы одно такое произведение 
# в последовательности есть.

f = open(r"D:\Downloads\27-A_2.txt")

N = f.readline()
kr1 = kr2 = kr7 = kr14 = 0
max_mul = 0
for line in f:
    val = int(line)

    if val%14 == 0:
        max_mul = max(max_mul, val*kr1, val*kr2, val*kr7, val*kr14)
        kr14 = max(kr14, val)
    elif val % 7 == 0:
        max_mul = max(max_mul, val*kr2, val*kr14)
        kr7 = max(kr7, val)
    elif val % 2 == 0:
        max_mul = max(max_mul, val*kr7, val*kr14)
        kr2 = max(kr2, val)
    else:
        max_mul = max(max_mul, val*kr14)
        kr1 = max(kr1, val)

print(max_mul)