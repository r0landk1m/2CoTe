n, m, v = map(int, input().split())
point = [list(map(int, input().split())) for _ in range(m)]
point.sort()

check_dfs = [1] * n
check_bfs = [1] * n
p_dfs = []

def dfs(s):
  print(s)
  check_dfs[s - 1] = 0
  for i in range(m):
    if m[i][0] == s:
      dfs(m[i][1])

dfs(v)