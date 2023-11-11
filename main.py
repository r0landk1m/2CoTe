# 어떠한 수 N이 1이 될 최소 과정 횟수
# 1. N에서 1을 뺸다.
# 2. N을 K로 나눈다.


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