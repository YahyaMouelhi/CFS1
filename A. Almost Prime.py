def prime(n):
    if n<=3:return True
    for i in range(2,n):
        if n%i == 0 : return False
    return True

def almost_prime(n):
    d = 0
    for i in range(1,n+1):
        if n%i and 