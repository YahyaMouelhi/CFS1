#def pgcd(a,b):
#    if a==b : return a
#    elif a>b : return pgcd(a-b,a)
#    else : return pgcd(a,b-a)
#def ppcm(a,b,x,y):
#    if a>b:
#        if a%b == 0 : return a
#        else : return ppcm(a+x,b,x,y)
#    else :
#        if b%a == 0 : return b
#        else : return ppcm(a,b+y,x,y)
#for _ in range(int(input())):
#    n = int(input())
#    j = True
#    for i in range(1,n+1):
#        for j in range(1,n+1):
#            if pgcd(i,j) + ppcm(i,j,i,j) == n : 
#                print(i,j)
#                j = False
#                break
#        if not j : break


def gcd(a, b):
    while b : a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_pairs(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if gcd(i, j) + lcm(i, j) == n:
                return i, j

num_tests = int(input())
for _ in range(num_tests):
    n = int(input())
    i, j = find_pairs(n)
    print(i, j)