n = int(input())
phones = [input() for i in range(n)]

p = ""
prefixes = []
for j in range(len(phones[0])):
    if p == "" : p = phones[0][j]
    elif p[0] == phones[0][j-1] : p += phones[0][j] 
    else : prefixes.append(p) ; p = ""
print(prefixes)