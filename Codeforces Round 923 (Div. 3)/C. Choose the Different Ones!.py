for _ in range(int(input())):
    
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    occ1 , occ2  = set() , set()
    c1 , c2 = 0 , 0

    for i in range(n):
        if a[i] <= k : occ1.add(a[i])

    for i in range(m):
        if b[i] <= k : occ2.add(b[i])

    if len(occ1) > len(occ2) :
        ocp1 = occ1.copy()
        for i in ocp1:
            if i in occ2 and len(occ1) > k//2:
                occ1.remove(i)
            else : break
    else:
        ocp2 = occ2.copy()
        for i in ocp2:
            if i in occ1 and len(occ2) > k//2:
                occ2.remove(i)
            else : break

    occf = occ1 | occ2
    print("YES" if len(occ1) >= k//2 and len(occ2) >= k//2 and len(occf) == k  else "NO")