a,b,c = int(input()),int(input()),int(input())
x = [a+b*c , a*(b+c) , a*b*c , (a+b)*c , a+b+c]
print(max(x))