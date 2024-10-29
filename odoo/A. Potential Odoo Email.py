em = input()
p1 = em[0:em.find("@")]
p2 = em[em.find("@")+1:em.find(".")]
p3 = em[em.find(".")+1:]
s = 0
for i in range(len(p1)):
    if "a" <= p1[i] <= "z" :
        s += 1
print("yes" if 2 <= len(p1) <= 4 and s == len(p1) and p2 == "odoo" and em.find("@") != -1 and em.find(".") != -1 and p3 == "com" else "no" )