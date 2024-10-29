#for _ in range(int(input())):
#n = int(input())
#a = list(map(int,input().split()))
#
#for j in range(n):
#    for i in range(n-1):
#        if a[i] > a[i+1]  : a[i] -= 1 ; a[i+1] += 1
#w,j = True,0
#while w and j<n : 
#    if a[j] == a[0] : j += 1
#    else : w = False
#print(a)
#print("YES" if w else "NO")



#for _ in range(int(input())):
#    n = int(input())
#    a = list(map(int,input().split()))
#    print("YES" if sum(a)%n == 0 else "NO")

#
#for _ in range(int(input())):
#    n = int(input())
#    a = list(map(int, input().split()))
#
#    sa = sum(a) // n
#
#    if sum(a) % n != 0 : print("NO")
#    else:
#        exc = [max(0, ai - sa) for ai in a]
#        defi = [max(0, sa - ai) for ai in a]
#        
#        if sum(exc) == sum(defi) : print("YES")
#        else : print("NO")
#



#n = int(input())
#a = list(map(int,input().split()))
#
#avg = sum(a)//n
#while any(x != avg for x in a):
#    for j in range(n):
#        for i in range(n-1):
#            if a[i] > a[i+1] and a[i] != avg : a[i] -= 1 ; a[i+1] += 1
#
#w,j = True,0
#while w and j<n : 
#    if a[j] == a[0] : j += 1
#    else : w = False
#
#print(a)
#print("YES" if w else "NO")



# correctt but slow :(

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    avg = sum(a) // n

    for i in range(n-1):
        for j in range(i+1,n):
            while a[i] > avg and a[i] > a[j] and a[j] < avg :
                a[i] -= 1
                a[j] += 1

    w,j = True,0
    while w and j<n:
        if a[j] != avg : w = False
        j += 1

    print("YES" if w else "NO")
