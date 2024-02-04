#00시 00분 00초 부터 n시 59분 59초 까지
#3이 하나라도 포함되어 있다면 카운트

n = int(input())

result = 0
for i in range(0, n+1, 1):
  for j in range(60):
    for k in range(60):
      if "3" in str(i) or "3" in str(j) or "3" in str(k):
        result += 1

print(result)

'''
h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      if "3" in str(i) + str(j) + str(k):
        count += 1

print(count)
'''