n = int(input())
s = [int(i) for i in input().split()]
s1 = [s[0]]
x = 0
for i in range(n):
    if i > 0 : 
        s1.append(s[i])
        if (s[i] == max(s1) or s[i] == min(s1)) and s1.count(s[i]) == 1:
            x += 1 
print(x)