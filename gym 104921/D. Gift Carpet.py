def cl(x):
    if len(x) == 1 : return x
    elif x[0] in "vika" : return cl(x[0]+x[1:])
    else : return cl(x[1:])

print(cl("vvvvvviiiiiiiikkkkkkkaaaaaaaaaa"))

l,c = map(int,input().split())
mx = [input() for i in range(l)]

if l<4 and c<4 : 
    print("NO")

for i in range(l):
    if "vika" in mx[i] or "vika" in cl(mx[i]): 
        print("YES")




















#def search(a):
#    for w in a:
#        cs = 0
#        for i in range(len(w)):
#            if w[i] == "vika"[cs] :
#                cs += 1
#                if cs == 4 : return True
#    return False
#
#for _ in range(int(input())):
#    l,c = map(int,input().split())
#    carpet = [input() for i in range(l)]
#
#    if l < 4 and c < 4 : print("NO")
#    else:
#        fs = []
#        for i in range(c):
#            w1 = ""
#            for j in range(l): 
#                if carpet[j][i] in "vika" : w1 += carpet[j][i]
#            fs.append(w1)
#
#        for i in range(l):
#            w2 = ""
#            for j in range(c):
#                if carpet[i][j] in "vika" : w2 += carpet[i][j]
#            fs.append(w2)
#
#        if search(fs) : print("YES")
#        else : print("NO")
#
#

#for k in range(int(input())):
#
    #n,m = map(int,input().split())
    #mx = [input() for i in range(n)]
    #if m < 4 and n < 4 : print("NO")
    #elif "vika" in mx : print("YES")
    #else:
    #    c,l = "",""
    #    for i in range(n):
    #        for j in range(m):
    #            if mx[i][j] in "vika" : c += mx[i][j]
    #    for i in range(m):
    #        for j in range(n):
    #            if mx[j][i] in "vika" : l += mx[i][j]
    #    if "vika" in c or "vika" in l : print("YES")
    #    else : print("NO")
#
    
    #if m < 4 and n < 4 : print("NO")
    #else : 
    #    r1,r2 = "",""
    #    for i in range(n):
    #        if "vika" in mx[i] or "vika" in r1 : break
    #        for j in range(m):
    #            try : 
    #                if mx[i][j] in "vika" : r1 += mx[i][j]
    #            except : break
    #    for i in range(m):
    #        if "vika" in r2 or "vika" in r1 : break
    #        for j in range(n):
    #            try : 
    #                if mx[i][j] in "vika"  : r2 += mx[j][i]
    #            except : break
    #    if r1 == "vika" or r2 == "vika" : print("YES")
    #    else : print("NO")