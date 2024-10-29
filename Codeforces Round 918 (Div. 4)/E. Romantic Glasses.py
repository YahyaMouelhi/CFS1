def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    end = False
    for i in range(n):
        s = 0
        for j in range(i,n):
            s += (arr[j] if arr.index(arr[j])%2 == 0 else -1*arr[j])
            if s == 0 : end = True ; break
        if end : break
            
    print("YES" if end else "NO")

for _ in range(int(input())):
    solve()