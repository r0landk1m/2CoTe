n, m = map(int, input().split())
frame = [list(map(int, input())) for _ in range(n)]

def dfs(graph, h, w):
  graph[h][w] = 1
  if h + 1 < n and graph[h + 1][w] == 0:
    dfs(graph, h + 1, w)
  if w + 1 < m and graph[h][w + 1] == 0:
    dfs(graph, h, w + 1)
  if h - 1 >= 0 and graph[h - 1][w] == 0:
    dfs(graph, h - 1, w)
  if w - 1 >= 0 and graph[h][w - 1] == 0:
    dfs(graph, h, w - 1)

result = 0
for i in range(n):
  for j in range(m):
    if frame[i][j] == 0:
      result += 1
      dfs(frame, i, j)

print(result)

'''
15 14  
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''