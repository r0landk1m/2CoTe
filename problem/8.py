s = list(input())
s.sort()
num_s = 0
count = 0

for i in s:
  if ord(i) < 65 or ord(i) > 90:
    num_s += int(i)
    count += 1

s = s[count:]

if num_s != 0:
  print(*s, num_s, sep = "")
else:
  print(''.join(s))

'''
K1KA5CB7

AJKDLSI412K4JSJ9D
'''

'''
data = input()
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)

result.sort()

if value != 0:
  result.append(str(value))

print(''.join(result))
'''