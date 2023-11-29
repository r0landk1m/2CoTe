'''
ex1)
3 2
1 1000
10 100
6 5
11
7
answer - 1100

ex2)
3 2
8 1000
6 5
10 100
10
7
answer - 1005

숫자에 가장 가까운 수이나 합이 가장 커야함.
But, for to for 을 사용하면 안됨.

weight 에 가장 가까운 수 중 가장 큰 수를 찾자.
ex2) 참조
10에 가까운 순 : 10 8 6
가장 큰 순: 8(1000) 10(100) 6(5)

ex1) 참조
11에 가까운 순 : 10 6 1
가장 큰 순 : 1(1000) 10(100) 6(5)

weight 이 작은 순으로 해본다면?
weight 에 가까운 순으로만 생각하면 안됨
'가까우면서 가장 큰 수'
'''

N, K = map(int, input().split())
jewel = []
weight = []
result = 0

for i in range(N):
  a,b=(map(int, input().split()))
  jewel-append

for j in range(K):
  weight.append(int(input()))

print(max(jewel[]))
