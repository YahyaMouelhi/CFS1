for _ in range(int(input())):
    n = input()
    c = 0
    d = "1"
    m = 1
    while True:
        if d*m == n : c += m ; break
        if m>3 : c += m ; m = 1 ; d = str(int(d)+1)
        else : c += m ; m += 1
    print(c)