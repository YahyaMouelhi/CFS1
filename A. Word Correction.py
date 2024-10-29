n = int(input())
w = input()
r = ""

i = 0
o = True
while i<n:
    if w[i] in "aeuioy" and o : r += w[i] ; o = False
    elif w[i] not in "aeuioy" : r += w[i] ; o = True
    i += 1

print(r)