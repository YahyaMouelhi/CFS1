n = int(input())
m = int(input())
s = int(input())
p = int(input())
total = p*3 + m*60*n + s*n
print(total//60)
print(total%60)