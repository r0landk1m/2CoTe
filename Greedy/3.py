# 어떠한 수 N이 1이 될 최소 과정 횟수
# 1. N에서 1을 뺸다.
# 2. N을 K로 나눈다.

N, K = map(int, input().split())

result = 0

while N != 1:
  if N % K == 0:
    N //= K
    result += 1
  else:
    N -= 1
    result += 1

print(result)

'''
1.
n, k = map(int, input().split())
result = 0

while n >= k:
  while n % k != 0:
    n -= 1
    result += 1
  n //= k
  result += 1

while n > 1:
  n -= 1
  result += 1

print(result)
2. 나눌 수 있을 때 까지 빼고 나누고 나눌 수 없는 수 합산
n, k = map(int, input().split())
result = 0

while True:
  target = (n // k) * k
  result += (n - target)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)
'''