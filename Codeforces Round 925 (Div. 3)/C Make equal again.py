import sys

for _ in range(int(input())):
    n = int(input())
    

    arr = list(map(int, input().split()))
    freq = [0] * (n + 1)
    for num in arr:
        freq[num] += 1
    
    target_value = max(freq)
    print(n - target_value)
