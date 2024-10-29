for p in range(int(input())):
    x = int(input())
    m,playing = 0,True
    while playing:

        if abs(x-1) % 3 == 0 or abs(x+1) % 3 == 0 :
            playing = False
            print("First")
        elif m >= 10 :
            playing = False
            print("Second")
        m += 1