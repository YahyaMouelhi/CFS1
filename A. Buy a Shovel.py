k,r = map(int,input().split())
p = 1
while k*p%10!=r and k*p%10!=0: p+= 1 
print(p)