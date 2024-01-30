n, m = map(int, input().split())
if m > n:
  m = n
book_loc = list(map(int, input().split()))
book_loc.sort()

neg = 0
pos = 0
if book_loc[n - 1] < 0:
  neg = n
else:
  for k in range(n):
    if book_loc[k] > 0:
      neg = k
      break
  pos = n - neg

result = 0
if abs(book_loc[0]) > book_loc[n - 1]:
  result -= abs(book_loc[0])
else:
  result -= book_loc[n - 1]

for i in range(0, neg, m):
  result += abs(book_loc[i]) * 2

book_loc.reverse()
for j in range(0, pos, m):
  result += book_loc[j] * 2

print(result)