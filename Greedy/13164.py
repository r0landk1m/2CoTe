n, k = map(int, input().split())
height = list(map(int, input().split()))
height_save = []

for i in range(n - 1):
  height_save.append(height[i + 1] - height[i])
height_save.sort()
del height_save[(n - k):]

print(sum(height_save))