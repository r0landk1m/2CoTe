n = list(map(int, input()))
half = len(n) // 2
front = 0
end = 0

for i in range(half):
  front += n[i]
  end += n[i + half]

if front == end:
  print("LUCKY")
else:
  print("READY")

'''
123402

7755
'''

'''
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
  summary += int(n[i])

for i in range(length // 2):
  summary -= int(n[i])

if summary == 0:
  print("LUCKY")
else:
  print("READY")
'''