for _ in range(int(input())):
    lb = input()
    lbs = list(set(lb))
    ln = len(lbs)
    s = False
    for i in range(3):
        if lb[i] == lb[i+1] : s = True
    if ln == 1 : print(-1)
    elif ln >= 3 or (ln == 2 and lb.count(lbs[0]) == lb.count(lbs[1])) : print(4)
    else : print(6)
    


#for i in range(int(input())):
#    lb = input()
#    if lb[0]==lb[1]==lb[2]==lb[3] : print(-1)
#    elif lb[0]!=lb[1]!=lb[2]!=lb[3] : print(4)
#    else:
#        freq = []
#        op = 0
#        for i in range(4):
#            if lb[i] in freq and lb[i-1] != lb[i] : op += 2
#            else : op += 1 ; freq.append(lb[i])
#        print(op)
