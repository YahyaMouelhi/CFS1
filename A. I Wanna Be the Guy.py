#level =  set(range(1, int(input()) + 1))
#x = list(map(int, input().split()))
#y = list(map(int, input().split()))
#x = set(x[1:])
#y = set(y[1:])
#print('I become the guy.' if level - (x | y) == set() else 'Oh, my keyboard!')

n = int(input())
a = list(map(int,input().split()))[1:] + list(map(int,input().split()))[1:]
a.sort()
a = list(set(a))
if list(range(1,n+1)) == a or list(range(0,n+1)) == a  : print("I become the guy.")
else : print("Oh, my keyboard!")