# 댜양한 수의 배열 중 M번 더하여 가장 큰 수 만들기
# 단, 특정 수가 연속 K번을 초과하여 더할 수 없다.

N, M, K = map(int, input().split())
num = list(set(map(int, input().split())))
T_num = 0

for a in range(len(num) - 1):
  for b in range(a, len(num)):
    if num[a] < num[b]:
      save = num[a]
      num[a] = num[b]
      num[b] = save

if len(num) == 1:
  T_num = num[0] * M
else:
  count = 0
  for c in range(M):
    if count == K:
      T_num += num[1]
      count = 0
    else:
      T_num += num[0]
      count += 1

print(T_num)

'''
1.
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)

2. 수열
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
'''