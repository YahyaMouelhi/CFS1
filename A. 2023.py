#def prdct(a):
#    s = 1
#    for i in a : s *= i
#    return s
#n,k = map(int,input().split())
#b,x = list(map(int,input().split())),2023
#divs = [1, 7, 17, 119, 289, 2023]
#for _ in range(n):
#    if x%b[_]==0 : x //= b[_]
#res,used = [],[]
#for i in range(k):
#    for idx in range(5,-1,-1):
#        if x%divs[idx] == 0 and divs[idx] not in used:
#            x //= divs[idx]
#            res.append(divs[idx])
#            if divs[idx] != 1 : used.append(divs[idx])
#            break
#pr = prdct(res+b)
#print(pr)
#print(res)
#print(used)
#if pr > 2023 : print("NO")
#else : print("YES")
#print(res)


#def prdct(a):
#    s = 1
#    for i in a : s *= i
#    return s
#
#for _ in range(int(input())):
#    n,k = map(int,input().split())
#    b = list(map(int,input().split()))
#    d = [1, 7, 17, 119, 289, 2023]
#    pr,xx,exist = prdct(b),2023,True
#    # basic check ...
#    for i in range(n):
#        if b[i] not in d : exist = False
#    if xx%pr != 0 or pr>2023 or not exist or pr not in d : print("NO") ; break
#    #work
#    if pr == 2023 : print("1 "*k)
#    else :
#        for i in range(k):
#            b.append(2023//prdct(b))
#            if prdct(b) == 2023 : print(i , "1 "*(k-i) ) ; break  


#n,m = map(int,input().split())
#a = map(int,input().split())
#d = [1, 7, 17, 119, 289, 2023]
#
#x,pr,imp = 2023,1,False
#for i in range(n):
#    if a[i] not in d : imp = True ; break
#    pr *= a[i]
#
#if pr>x or x%pr != 0 or imp : print("NO") 
#else :
#    res = []
#    for i in range(m):
#        if x//(pr*(x//pr)) == 1 : res.append(x//pr) ; x//=(x//pr) 
#
#

#d = [2023,289,119,17,7,1]
#for _ in range(int(input())):
#     n,k = map(int,input().split())
#     arr = list(map(int,input().split()))
#     pr,x = 1,2023
#     for i in range(n): pr *= arr[i]
#     if pr>2023 or 2023%pr!=0 : print("NO")
#     else:
#          print("YES")
#          x//=pr
#          r,w = "",True
#          while x>1 and k>1 and w:
#               for i in range(6):
#                    if x%d[i] == 0 and k>0 and d[i]*x==2023:
#                         r += f"{d[i]} "
#                         print(d[i])
#                         x//=d[i]
#                         k-=1
#                    else : w = False
#          print(r + "1 "*k)

for _ in range(int(input())):
     n,k = map(int,input().split())
     a = list(map(int,input().split()))
     pr = 1
     for i in range(n) : pr*=a[i]
     if 2023%pr != 0 : print("NO")
     else : print("YES");print(2023//pr , "1 "*(k-1))