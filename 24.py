f = open("24.txt")

s = f.readline() + '$'

i = 0
max_l = 0
r = -1
while i < len(s):
    l = 0
    if s[i] == 'Z':
        i += 1
        l += 1
        while s[i] in "XY" and s[i] != s[i-1]:
            i += 1
            l += 1
        max_l = max(max_l, l)
        if(l == 19):
            r = i
        # print(l)
    else:
        i += 1

print(max_l, r)