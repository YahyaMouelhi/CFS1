# CV - CVC

def solve():
    n = int(input())
    s = input()
    r = ""
    for i in range(n):
        r+=s[i]
        try :
            if (s[i] in "ea" and s[i+1] in "bcd" and s[i+2] in "ea") or (s[i] in "bcd" and s[i-1] in "ea" and s[i+1] in "bcd") : r += "." 
        except : pass
    print(r)

for _ in range(int(input())):
    solve()