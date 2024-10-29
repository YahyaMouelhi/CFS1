for i in range(int(input())):
    r = int(input())
    if r >= 1900 : print("Division 1")
    elif 1600 <= r <= 1899 : print("Division 2")
    elif 1400 <= r <= 1599 : print("Division 3")
    else : print("Division 4")