def pgcd(a,b):
    if a>b:
        if a%b==0 : return b
        elif a>b : return pgcd(a-b,b)
        else : return pgcd(a,b-a)
    else :
        if b%a==0 : return a
        elif a>b : return pgcd(a-b,b)
        else : return pgcd(a,b-a)


y,w = map(int,input().split())
p = 7-max(y,w)
x = 6
pg = pgcd(p,x)
print(f"{p//pg}/{x//pg}")