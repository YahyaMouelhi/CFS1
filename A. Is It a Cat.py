def cl(x):
    if len(x) <= 1 : return x
    elif x[0] == x[1]  : return cl(x[1:])
    else : return x[0] + cl(x[1:])

for _ in range(int(input())):
    n = int(input())
    s = cl(input().lower())
    print('YES' if 'meow' == s else 'NO')