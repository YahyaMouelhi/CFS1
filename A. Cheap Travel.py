
# can just take from n , or just n , or mixed !!!

from math import ceil
x = input().split()
n,m,a,b = int(x[0]),int(x[1]),int(x[2]),int(x[3])

np = n*a
mp = ceil(n/m)*b

#print(np)
#print(mp)

if np<mp : print(mp)
elif np>=mp : print(np)