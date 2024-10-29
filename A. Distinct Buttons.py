for x in range(int(input())):
    n = int(input())
    s = [list(map(int,input().split())) for i in range(n)]
    u,d,l,r = 0,0,0,0
    for m in s:
        if m[0] > 0 : r += m[0]
        else : l += m[0]
        if m[1] > 0 : u += m[1]
        else : d -= m[1]
    if u and d and l and r : print("NO")
    else : print("YES") 