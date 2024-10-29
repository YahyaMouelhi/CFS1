def product(a,n):
    r = 1
    for i in range(n): r *= a[i]
    return r

for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a[a.index(min(a))] += 1
    print(product(a,n))