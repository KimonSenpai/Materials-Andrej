# 105 kompege

f = open(r"D:\Downloads\24 (3).txt")

s = f.readline() + '$'

c = s[0]
l = 1
max_l = 0
max_c = 'q'

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        l += 1
    else:
        if max_l < l:
            max_l = l
            max_c = c
        
        c = s[i]
        l = 1

print(max_l, max_c)