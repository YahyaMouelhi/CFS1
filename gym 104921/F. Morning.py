#n = int(input())
#s = input().split()
db = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":10}
r = "1234567890"
for i in range(int(input())):
    x = input()
    m = db[x[0]]-1
    m += abs(db[x[0]]-db[x[1]])
    m += abs(db[x[1]]-db[x[2]])
    m += abs(db[x[2]]-db[x[3]])
    print(m+4)

#m = 4 + int(x[0])-1
#for i in range(4):
#    if x[i] == "0" :
#        if i == 0 :
#            if int(x[i+1]) != 0 : m += 10 - int(x[i+1])
#        if i == 3 : 
#            if int(x[i-1]) != 0 : m += 10 - int(x[i-1])
#        else : 
#            if int(x[i+1]) != 0 : m += 10 - int(x[i+1])
#            if int(x[i-1]) != 0 : m += 10 - int(x[i-1])
#    elif i == 0 : 
#        if int(x[i+1]) != 0 : m += abs( int(x[i]) - int(x[i+1]) )
#        else :  m += abs( int(x[i]) - 10 )
#    elif i == 3 : 
#        m += abs( int(x[i]) - int(x[i-1]) ) 
#        if int(x[i-1]) != 0 : m += abs( int(x[i]) - int(x[i-1]) )
#        else :  m += abs( int(x[i]) - 10 )
#    else : 
#        if int(x[i+1]) != 0 : m += abs( int(x[i]) - int(x[i+1]) )
#        if int(x[i-1]) != 0 : m += abs( int(x[i]) - int(x[i-1]) )
#print(m)
