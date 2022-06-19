f = open("26.txt")

K, N = map(int, f.readline().split())

places = [0]*K

for i in range(K):
    places[i] = int(f.readline())

stud = [[] for _ in range(K)]

for i in range(N):
    score, ind = map(int, f.readline().split())

    stud[ind] += [score]

for lst in stud:
    lst.sort(reverse=True)

count = 0
min_points, max_comp = 400, 1
for i in range(K):
    count += min(places[i], len(stud[i]))
    if len(stud[i])/places[i] > max_comp:
        max_comp = len(stud[i])/places[i]
        min_points = stud[i][places[i] - 1]
    elif len(stud[i])/places[i] == max_comp:
        min_points = min(min_points, stud[i][places[i] - 1])
print(count, min_points)

