n = int(input())
r = [list(map(int,input().split())) for i in range(n)]
e = 0
for i in r:
    if i[0]+2 <= i[1]:
        e += 1
print(e)