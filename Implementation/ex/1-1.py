#n - n*n 정사각형
#정사각형을 벗어나면 이동 무효
#x, y 반전 (y, x)로 표현

n = int(input())
plan = list(map(int, input().split()))

result = [0]*2

for i in plan:
  if i == "L":
    result[0] += 1
  elif i == "R":
    result[0] -= 1
  elif i == "U":
    result[1] += 1
  else i == "D":
    result[1] -= 1

  for j in result:
    if j < 1:
      j += 1
    elif j > n:
      j -= 1

print(*result)

'''
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ["L", "R", "U", "D"]

for plan in plans:
  for i in range(len(move_type)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x, y)
'''