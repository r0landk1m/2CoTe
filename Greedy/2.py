# 숫자 카드가 N * M 형태로 놓여있다. (N - 행, M - 열)
# 뽑고자 하는 카드 행을 선택
# 선택된 행에 가장 숫자가 낮은 카드 뽑기

N, M = map(int, input().split())
num = [[0 for _ in range(N)] for _ in range(M)]

for a in range(N):
  num[a] = list(map(int, input().split()))
  num[a].sort()

result = 0
for a in range(N):
  if num[a][0] > result:
    result = num[a][0]

print(result)

'''
1. min()
n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)
2. 2중 반복문
n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  result = max(result, min_value)

print(result)
'''