n, k = map(int, input().split())
num = list(map(int, input()))
save = num.copy()
save.sort()

for i in range(k):
  num.remove(save[i])

print(*num, sep="")