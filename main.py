import sys
input = sys.stdin.readline

n = int(input())
class_num = []
for _ in range(n):
  class_num.append(list(map(int, input().split())))
class_num.sort()

result = 1
save = [class_num[0][1]]
for i in range(1, n):
  if class_num[i][0] >= save[0]:
    save[0] = class_num[i][1]
  else:
    save.append(class_num[i][1])
    result += 1
  save.sort()

print(result)