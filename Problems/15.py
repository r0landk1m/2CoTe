n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

def dfs(r, s, c, vc, g):
  if vc[s] > c or vc[s] == 0:
    vc[s] = c
  c += 1

  if r >= c:
    for i in g[s]:
      dfs(r, i, c, vc, g)

count = 0
visited_count = [0] * (n + 1)
dfs(k, x, count, visited_count, graph)

check = 0
for j in range(len(visited_count)):
  if visited_count[j] == k:
    check += 1
    print(j)

if check == 0:
  print(-1)

'''
4 4 2 1
1 2 
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4
'''

'''
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
  now = q.popleft()
  for next_node in graph[now]:
    if distance[next_node] == -1:
      distance[next_node] = distance[now] + 1
      q.append(next_node)

check = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)
'''