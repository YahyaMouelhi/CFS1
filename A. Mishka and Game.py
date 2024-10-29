mm,mc,d = 0,0,0
for _ in range(int(input())):
    m,c = map(int,input().split())
    if m>c : mm+=1
    elif c>m : mc+=1
    else : d +=1
if mm>mc:print("Mishka")
elif mc>mm:print("Chris")
else:print("Friendship is magic!^^")