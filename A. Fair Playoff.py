for _ in range(int(input())):
    s1,s2,s3,s4 = map(int,input().split())
    if ((s1<s3 and s1<s4) and (s2<s3 and s2<s4)) or ((s1>s3 and s1>s4) and (s2>s3 and s2>s4)) : print("NO")
    else : print("YES")