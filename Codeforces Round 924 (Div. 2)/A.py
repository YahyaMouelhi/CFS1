for _ in range(int(input())):
    a,b = map(int,input().split())
    if (a == 1 and b<=2) or (b == 1 and a<=2) : print("NO")
    elif (a%2 == 0 and b%2 == 0 and a!=b) or (a%2==0 and a//2 != b) or (b%2==0 and b//2 != a) : print("YES")
    else : print("NO")