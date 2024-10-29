alph = "abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):
    n = int(input())
    if 2 < n <= 28 : print("aa"+alph[(n-3)%26])
    elif 28 < n <= 52 : print("a"+alph[(n-28)%26]+"z")
    else : print(alph[(n-53)%26]+"zz")