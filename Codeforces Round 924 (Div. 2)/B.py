for _ in range(int(input())):
    n = int(input())
    arry = list(map(int,input().split()))
    arry.sort()
    perm = list(range(n,0,-1))
    res = [perm[i]+arry[i] for i in range(n)]

    freq = {}
    for i in range(n):
        if arry[i] in freq : freq[arry[i]] += 1
        else : freq[arry[i]] = 1
    #print(freq)
    for i in range(n):
        if res[i] in freq : freq[res[i]] += 1
        else : freq[res[i]] = 1 # el star edha naan zok omk zedtk f 10 sec remaining :()

    #print(res)
    #print(freq)
    print(max(freq.values()))

    # fuck before submission zok wa9t wfee naaaan din zebi