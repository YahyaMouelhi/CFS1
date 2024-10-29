n = int(input())
s = list(map(int,input().split()))

pmx = s.index(max(s))
pmn , mx , mn = 0 , max(s) , s[0]
for i in range(n):
    if s[i] <= mn :
        pmn = i
        mn = s[i]

if pmn > pmx : print(pmx+n-1-pmn)
else : print(pmx+n-2-pmn)