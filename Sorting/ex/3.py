n, k = map(int, input().split())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

array_A.sort()
array_B.sort(reverse=True)

for i in range(k):
  #빼먹은 부분
  if array_A[i] < array_B[i]:
  #-------------------
    array_A[i], array_B[i] = array_B[i], array_A[i]
  else:
    break

print(sum(array_A))

'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
'''

'''
5 3
1 2 5 4 3
5 5 6 6 5
'''