crane_n = int(input())
crane = list(map(int, input().split()))
box_n = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

if max(box) > max(crane):
  print(-1)
else:
  result = 0
  save = 0
  while save < box_n:
    for i in range(crane_n):
      for j in range(len(box)):
        if crane[i] >= box[j]:
          save += 1
          box.remove(box[j])
          break
    result += 1

  print(result)