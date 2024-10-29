n , k = map(int,input().split())
t , p = 240 - k , 0
for i in range(1,n+1):
    if t-(5*i) >= 0 :
        p += 1
        t -= 5*i
    else : break
print(p)