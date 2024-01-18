n = int(input())
word = []
for _ in range(n):
  word.append(input())
word.sort(key = len, reverse = True)
max_len = len(word[0])
for p in range(1, n):
  word[p] = word[p].zfill(max_len)
alpha = [0] * 26

for i in range(max_len):
  for j in range(n):
    if word[j][i] != "0":
      alpha[ord(word[j][i]) - 65] += (10 ** (max_len - 1 - i))
alpha.sort(reverse = True)

result = 0
count = 9
q = 0
while alpha[q] != 0:
  if count == -1:
    break
  result += alpha[q] * count
  count -= 1
  q += 1

print(result)