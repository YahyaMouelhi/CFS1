for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    s1,s2 = 0,0
    for i in range(n-1):
        if s[i] < 0 : s2 += s[i]
        else : s1 += s[i]
    print((s1+s2)*-1)