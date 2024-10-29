for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    r = 0
    for i in range(n-1):
        if a[i] > a[i+1] : r += a[i]-a[i+1]
    print(r)