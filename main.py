#적은 수부터 해겷해야 하는 문제

from collections import deque

n, m, v = map(int, input().split())
point = [list(map(int, input().split())) for _ in range(m)]

check_dfs = [0] * (n + 1)
check_bfs = [0] * (n + 1)

def dfs(s, p, check):
  if check[s] == 0:
    check_dfs[s] = 1
    print(s, end =" ")
  else:
    return
  save = n
  for i in p:
    if i[0] == s and i[1] < save and check[i[1]] == 0:
      save = i[1]
    if i[1] == s and i[0] < save and check[i[0]] == 0:
      save = i[0]
  dfs(save, p, check)

def bfs(s, p, check):
  queue = deque([s])
  check[s] = 1
  while queue:
    num = queue.popleft()
    print(num, end=" ")
    save = n
    for i in p:
      if i[0] == num and i[1] < save and check[i[1]] == 0:
        save = i[1]
      if i[1] == num and i[0] < save and check[i[0]] == 0:
        save = i[0]
    queue.append(save)
    check[save] = 1

dfs(v, point, check_dfs)
print("")
bfs(v, point, check_bfs)

