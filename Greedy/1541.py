import re

text = input()
num = re.findall(r'\d+', text)
result = int(num[0])
count = 1

for a in range(len(text)):
  if text[a] == "+":
    result += int(num[count])
    count += 1
  elif text[a] == "-":
    break

for b in range(count, len(num)):
  result -= int(num[b])

print(result)