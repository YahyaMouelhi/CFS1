for _ in range(int(input())):
    s = [input() for i in range(3)]
    x = "ABC"
    for i in range(3):
        for j in range(3):
            if x[i] not in s[j]:
                print(x[i]) 