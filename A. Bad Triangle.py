for t in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    a,b,c,w = 0,0,0,0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a,b,c = s[i],s[j],s[k]
                if a+b>c or a+c>b or b+c>a : 
                    print(f"{a} {b} {c}")
                    w += 1
                    break
            if w != 0 : break
        if w != 0 : break

    if w == 0 : print(-1)