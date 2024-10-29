def solve(n, k):
    if (n - 1) ** 2 + 1 == k:
        return 1  
    if k % 2 == 0:
        return k // 2  
    return k // 2 + 1  

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))