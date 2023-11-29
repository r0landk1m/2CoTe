n = int(input())
card_set = []
for _ in range(n):
  card_set.append(int(input()))
card_set.sort()

result = 0
while len(card_set) != 1:
  save = card_set[0] + card_set[1]
  result += save
  card_set[1] = save
  del card_set[0]
  card_set.sort()

print(result)