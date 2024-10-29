t = int(input())
moves = [input() for i in range(t)]
letters = "abcdefgh"

for k in range(t):
    l = moves[k][0]
    n = int(moves[k][1])
    for i in range(1,9):
        if i != n : print(l+str(i))
        if l != letters[i-1] : print(letters[i-1]+str(n))