def sort(d,n):
    ech = True
    while ech :
        ech = False
        for i in range(n-1):
            if d[i][0] > d[i+1][0] :
                tmp = d[i]
                d[i] = d[i+1]
                d[i+1] = tmp 
                ech = True

s,n = map(int,input().split())
d = [ list(map(int,input().split())) for i in range(n) ]
sort(d,n)
p = True
for i in range(n):
    if s - d[i][0] > 0 : s += d[i][1] 
    else :
        p = False
        break
print("YES" if p else "NO")