for i in range(int(input())):
    a,b,c = map(int,input().split())
    if a+b == c or a+c == b or b+c == a : print("YES")
    elif (a%2 == 0 and b+a//2 == c+a//2) or (b%2 == 0 and a+b//2 == c+b//2)  or (c%2 == 0 and a+c//2 == b+c//2) : print("YES")
    else : print("NO")  