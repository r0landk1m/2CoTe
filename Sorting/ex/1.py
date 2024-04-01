n = int(input())
num = []

for _ in range(n):
  num.append(int(input()))

num.sort(reverse = True)
print(num)

'''
n = int(input())

array = []
for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
  print(i, end=' ')
'''

'''
3
15
27
12
'''