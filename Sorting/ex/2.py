n = int(input())

student = [["a", 0] for _ in range(n)]
for i in range(n):
  name, score = input().split()
  student[i][0] = name
  student[i][1] = int(score)

student.sort(key = lambda x: x[1])
for j in range(n):
  print(student[j][0], end = " ")

'''
n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  #리스트 속에 튜플로 저장
  array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
  print(student[0], end=' ')
'''

'''
2
홍길동 95
이순신 77
'''