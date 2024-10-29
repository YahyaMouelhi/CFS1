#def search(arr,x):
#    mid = len(arr)//2
#    if len(arr) == 0 : return False
#    if arr[mid] == x : return True
#    elif arr[mid] < x : return search(arr[mid+1:],x)
#    else : return search(arr[:mid],x)

# accepted code (both correct , but recursion takes more time and memory)

#n,k = map(int,input().split())
#a = list(map(int,input().split()))
#q = list(map(int,input().split()))
#
#for i in range(k):
#    x = q[i]
#    left,right,found = 0,n-1,False
#    while left <= right and not found:
#        mid = (left + right) // 2
#        if a[mid] == x : found = True
#        elif a[mid] < x : left = mid + 1
#        else : right = mid - 1
#    print("YES" if found else "NO")


arr = [10,12,15,19,26,28,34,36,37,39,48,49,51,53,59,61,61,67,99]
n = len(arr)
x = 15

l,r = 0,n-1
f = False
pos = 0
while l<=r and not f:
    m = (l+r)//2
    if arr[m] == x : f,pos = True,m
    elif arr[m] > x : r = m-1
    else : l = m+1

print(pos if f else "NO")