n = int(input())
ward_num = []
for _ in range(n):
  ward_num.append(input())
ward_num.sort(key = len, reverse = True)

