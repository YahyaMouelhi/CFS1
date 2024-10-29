for _ in range(int(input())):
    n = int(input())
    if (n%2 == 0 and n%3) or n%2 == 0 == 0 : print("NO")
    elif n%3 == 0 or n%5 == 0 or n%7 == 0 or n%11: print("YES") 
    else : print("NO")