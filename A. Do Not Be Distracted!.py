n = int(input())
task = list(input())
deja = {task[0]:1}
dist = False
for i in range(1,n):
    if task[i] in deja and task[i] == task[i-1] : deja[task[i]] += 1
    elif task[i] not in deja and task[i-1] != task[i] : deja[task[i]] = 1
    else : dist = True ; break
print("YES" if dist else "NO")

#WRONG ....