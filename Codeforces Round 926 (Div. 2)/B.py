for _ in range(int(input())):
    n,k = map(int,input().split())
    print(n*2 if k == 4*n - 2 else (k//2) + k%2)


    # FUCK THIS PROBLEM FFFFFUUUUUUUUCKCKCKCKCK :(((

#for _ in range(int(input())):
#    n,k = map(int,input().split())
#    d = n*4-2
#    print(k//2 if 1 else k//2+1)
#

    #if k<=(n*4-2)*2 or (n*4)*2-2 < k <= n*8  : print(k//2 if k%2==0 and (k//2)%2 == 0 else k//2+1)
    #else : print((k//2)*2 if k%2==0 else (k//2)*2+1)