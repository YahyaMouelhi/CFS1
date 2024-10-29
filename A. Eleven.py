def f(x):
    if x<=2 : return 1
    else :  return f(x-2)+f(x-1)

def ff(x):
    j = 1
    t = f(j)
    while t<x :
        j += 1
        t = f(j)
    return t==x

n = int(input())
res = ["O" if ff(i) else "o" for i in range(1,n+1)]
print("".join(res))