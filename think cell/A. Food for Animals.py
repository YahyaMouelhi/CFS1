for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    score = 0
    i = 0
    while i<n :
        m1 = min(arr)
        arr.remove(m1)
        m2 = min(arr)
        arr.remove(m2)
        score += min(m1,m2)
        i += 1
    print(score)