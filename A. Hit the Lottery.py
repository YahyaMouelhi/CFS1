x = int(input())
papers = [100,20,10,5,1]
bills = 0

for i in range(5):
    bills += x//papers[i]
    x %= papers[i]

print(bills)
