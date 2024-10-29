for _ in range(int(input())):
    n = int(input())
    s = 0
    while n>0:
        while s%3 == 0 or s%10 == 3 : s += 1
        s += 1
        n-= 1
    print(s-1)