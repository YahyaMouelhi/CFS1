for _ in range(int(input())):
    h,m = map(int,input().split())
    print( 1440 - (m + h * 60))