for _ in range(int(input())):
    n = int(input())
    p = input()
    c = 0
    for i in range(n-1):
        if p[i] == "@" : c += 1
        elif p[i] == "*" and p[i+1] == "*" : break
        if i==n-2 and p[n-1] == "@" : c += 1
    print(c) 