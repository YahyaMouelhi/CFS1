"""
000 - 111
011 - 211
101 - 121
110 - 112
123 - 320
112 - 
"""
for _ in range(int(input())):
    v = list(map(int,input().split()))
    mx = max(v)
    if v[0] == v[1] == v[2] == mx : print("1 1 1")
    elif v[1] == v[2] and v[2] == mx : print(f"{mx+1-v[0]} 1 1")
    elif v[0] == v[2] and v[2] == mx : print(f"1 {mx+1-v[1]} 1")
    elif v[0] == v[1] and v[1] == mx : print(f"1 1 {mx+1-v[2]}")
    else :
        for i in range(3):
            if v[i] == max(v) : print(0 , end=" ")
            else : print(max(v)+1-v[i] , end = " ")
        print()