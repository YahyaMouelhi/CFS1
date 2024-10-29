def solve(n, k):
  if n == 3 and k >= 4:
    return 3
  max_cells_needed = (n - 1) ** 2 + 1

  if k >= max_cells_needed:
    return max_cells_needed

  if k % 2 == 0:
    return k // 2

  return k // 2 + 1

t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  print(solve(n, k))
