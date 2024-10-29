s = [int(input()) for i in range(5)]
total = s[0]*s[1]*s[2]
print((total//s[3])*s[4] if total%s[3]==0 else (total//s[3])*s[4]+s[4])