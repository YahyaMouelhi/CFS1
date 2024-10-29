
for _ in range(int(input())):
    n,s,r = int(input()),input(),0
    if s[0] == "B" and s[-1] == "B" : 
        r = n
    else : 
        p,f = 0,0
        for i in range(n):
            if s[i] == "B" :
                p = i
                break
        for i in range(n-1,0,-1):
            if s[i] == "B" : 
                f = i
                break
        r = f-p+1
    print(r) 