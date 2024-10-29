for i in range(int(input())):
    s,r = "".join([input() for i in range(8)]),""
    for i in range(64):
        if s[i] != "." : r += s[i]
    print(r)