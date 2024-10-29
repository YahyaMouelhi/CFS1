#k = int(input())
#l = int(input())
#m = int(input())
#n = int(input())
#d = int(input())
#r = [i for i in range(1,d+1) if i%k==0 or i%l==0 or i%m==0 or i%n==0]
#print(len(r))


#s = [int(input()) for i in range(5)]
#r = [i for i in range(1,s[4]+1) if i%s[0]==0 or i%s[1]==0 or i%s[2]==0 or i%s[3]==0]
#print(len(r))

s,r = [int(input()) for i in range(5)],0
for i in range(1,s[4]+1):
    if i%s[0]==0 or i%s[1]==0 or i%s[2]==0 or i%s[3]==0: r+= 1
print(r)