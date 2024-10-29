s,c = list(map(int,input().split())),0
s.sort()
for i in range(3) : 
    if s[i] == s[i+1] : c += 1
print(c)