for _ in range(int(input())):
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    c = 0
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]+a[j])%x==0 or (a[i]-a[j])%y==0 and a[i]-a[j] > 0 : c += 1
    print(c)