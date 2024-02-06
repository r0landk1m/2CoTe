#n * m 크기의 직사각형 맵
#맵의 각 칸은 (A, B) x = B, y = A
#캐릭터 정면 기준 왼쪽부터 이동 가능 여부 확인
#불가 시 왼쪽 회전, 아예 없다면 뒤로 이동

n, m = map(int, input().split())
a, b, d = map(int, input().split())
map_size = [list(map(int, input().split())) for _ in range(n)]
#북, 동, 남, 서
move = [[0, -1], [-1, 0], [0, 1], [1, 0]]
back = [[1, 0], [0, -1], [-1, 0], [0, 1]]

result = 1
while True:
  count = 0
  for i in range(4):
    print(i, "--------------------------")
    ad = a + move[d][0]
    bd = b + move[d][1]

    if d == -4:
      d = 0

    if ad >= 0 and bd >= 0 and map_size[ad][bd] < 1:
      print(ad, bd, d)
      result += 1
      #0 = 안가봄, 1 = 바다, 2 = 가봄
      map_size[a][b] = 2
      a = ad
      b = bd
      d -= 1
      print(map_size)
      break
    else:
      d -= 1
      count += 1

  if count == 4:
    if map_size[a + move[(d - 2)][0]][b + move[(d - 2)][1]] != 1:
      a += move[(d - 2)][0]
      b += move[(d - 2)][1]
    else:
      break

print(result)