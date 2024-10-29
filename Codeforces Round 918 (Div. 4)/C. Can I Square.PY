from math import sqrt

def solve():
    n = int(input())
    s = sqrt(sum(list(map(int,input().split()))))
    print("NO" if s != int(s) else "YES")

for _ in range(int(input())):
    solve()