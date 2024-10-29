n = int(input())
s = [input().lower() for i in range(n)]
for i in s:
    if "yes" in i : print("YES")
    else : print("NO")