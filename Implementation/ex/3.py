#n * m 크기의 직사각형 맵
#맵의 각 칸은 (A, B) x = B, y = A
#캐릭터 정면 기준 왼쪽부터 이동 가능 여부 확인
#불가 시 왼쪽 회전, 아예 없다면 뒤로 이동

n, m = map(int, input().split())
a, b, d = map(int, input().split())
map_size = [list(map(int, input().split())) for _ in range(n)]
#북, 동, 남, 서
move = [[0, -1], [-1, 0], [0, 1], [1, 0]]
back = [[0, 1], [1, 0], [0, -1], [-1, 0]]

result = 1
while True:
  count = 0
  for i in range(4):
    #print(i, "--------------------------")
    ad = a + move[d][0]
    bd = b + move[d][1]

    if d == -4:
      d = 0

    if ad >= 0 and bd >= 0 and map_size[ad][bd] < 1:
      #print(ad, bd, d)
      result += 1
      #0 = 안가봄, 1 = 바다, 2 = 가봄
      map_size[a][b] = 2
      a = ad
      b = bd
      d -= 1
      #print(map_size)
      break
    else:
      d -= 1
      count += 1

  d += 4
  if count == 4:
    if map_size[a + back[d][0]][b + back[d][1]] != 1:
      a += back[d][0]
      b += back[d][1]
    else:
      break

print(result)

'''
n, m = map(int, input().split())
d = [[0 * m for _ in range(n)]] #방문 여부 확인
x, y, direction = map(int, input().split())
d[x][y] = 1 #시작 좌표 방문 처리

array = []
for i in range(n):
  array.append(list(map(int, input().split())))

#북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#회전
def turn_left():
  global direction
  dirction -= 1
  if direction = 3
    direction = 3

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
  turn_time += 1

  #네 방향 모두 이동 불가
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    #후방 이동 가능여부 확인
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)
'''