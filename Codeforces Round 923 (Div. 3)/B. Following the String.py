llc = "abcdefghijklmnopqrstuvwxyz"
for t in range(int(input())):
    db = {}
    n = int(input())
    s = input().split()
    res = ""
    for i in range(n):
        if not s[i] in db : 
            db[s[i]] = 1
            res += "a"
        else : 
            res += llc[db[s[i]] % 26]
            db[s[i]] += db[s[i]] 

    print(res)
