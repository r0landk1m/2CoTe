n = int(input())
num_p = []
num_m = []
count = 0
for _ in range(n):
  save = int(input())
  if save > 0:
    num_p.append(save)
  elif save == 0:
    count = 1
  else:
    num_m.append(save)

num_p.sort(reverse = True)
num_m.sort()
if count == 1 and len(num_m) % 2 == 1:
  num_m.remove(max(num_m))

result = 0
cri = 0
save = 0
for p, i in enumerate(num_p):
  if i == 1:
    result += save + 1
    save = 0
  else:
    if cri == 0:
      save += i
      cri += 1
      if p == len(num_p) - 1:
        result += save
    else:
      save *= i
      result += save
      save = 0
      cri = 0

cri = 0
save = 0
for p, i in enumerate(num_m):
  if p == len(num_m) - 1:
    if len(num_m) % 2 == 1:
      result += i
    else:
      result += i * save
  else:
    if cri == 0:
      save += i
      cri += 1
    else:
      save *= i
      result += save
      save = 0
      cri = 0

print(result)