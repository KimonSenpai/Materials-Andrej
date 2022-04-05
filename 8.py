
# 0 - 4 - согл
# 5 - 7 - гл


sogl = {str(i) for i in range(5)}
gl = {str(i) for i in range(5, 8)}
def check(val):
    sval = oct(val)[2:]
    if sval[0] in sogl:
        return False
    if sval[0] == '5' and sval[1] in sogl or sval[6] == '5' and sval[5] in sogl:
        return False
    for i in range(1, 6):
        if sval[i] == '5' and (sval[i - 1] in sogl or sval[i + 1] in sogl):
            return False
    return True

count = 0

for i in range(8**6, 8**7):
    if check(i):
        count += 1

print(count)
