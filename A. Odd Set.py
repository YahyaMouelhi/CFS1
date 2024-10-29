for _ in range(int(input())):
    n,a = int(input()),list(map(int,input().split()))
    odds = [a[i] for i in range(n*2) if a[i]%2!=0]
    pairs = [a[i] for i in range(n*2) if a[i]%2==0]
    print(odds)
    print(pairs)
    print(f"sum odds = {sum(odds)} len = {len(odds)} , sum pairs = {sum(pairs)} len = {len(pairs)} ")
    if len(odds)<n or len(pairs)<n : print("NO")
    elif sum(odds)%2==0 or sum(pairs)%2==0 : print("NO")
    else : print("YES")

# abondonnedd ;)