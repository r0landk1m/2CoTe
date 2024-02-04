#8 * 8 좌표로 이뤄진 정원
#나이트의 위치가 주어졌을 때 이동 가능한 경우

l = input()

hight = min(104 - ord(l[0]), ord(l[0]) - 97)
width = min(8 - int(l[1]), int(l[1]) - 1)
if hight >= 2:
  hight = 2
if width >= 2:
  width = 2

print(2 ** hight + 2 ** width)

'''
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)
'''