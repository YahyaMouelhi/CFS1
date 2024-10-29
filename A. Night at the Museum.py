s = input()
alph = "abcdefghijklmnopqrstuvwxyz"
c = 0

pos = 0
for i in range(len(s)):
    c += abs(26-(alph.find(s[i])-pos)) if abs(26-(alph.find(s[i])-pos))<13 else alph.find(s[i]) 
    alph = alph[abs(26-(alph.find(s[i])-pos)):]+alph[:abs(26-(alph.find(s[i])-pos))] if  abs(26-(alph.find(s[i])-pos))<13 else alph[alph.find(s[i]):]+alph[:alph.find(s[i])]
    pos = abs(26-(alph.find(s[i])-pos)) if abs(26-(alph.find(s[i])-pos))<13 else alph.find(s[i]) 

print(c)