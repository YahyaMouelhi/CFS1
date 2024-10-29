for _ in range(int(input())):
    a,b,c = input().split()
    if a==b : print(c)
    elif a==c: print(b)
    else : print(a)