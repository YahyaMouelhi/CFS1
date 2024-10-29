n = int(input())
s = list(map(int,input().split()))
s = [abs(s[i]) for i in range(n)]
print(min(s))