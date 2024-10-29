teams = {}
for i in range(int(input())):
    s = input()
    if s in teams : teams[s] += 1
    else : teams[s] = 1

mx,te = 0,""
for k in teams:
    if teams[k] > mx : 
        te,mx = k,teams[k]
print(te)