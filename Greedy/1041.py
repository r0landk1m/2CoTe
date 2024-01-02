n = int(input())
num = list(map(int, input().split()))

if n == 1:
  num.remove(max(num))
  print(sum(num))
else:
  n_list = [[0, 1, 2], [0, 2, 4], [1, 2, 5], [2, 4, 5], [0, 1, 3], [0, 3, 4], [1, 3, 5], [3, 4, 5]]
  n_min = 150
  save = []

  for i in n_list:
    n_sum = num[i[0]] + num[i[1]] + num[i[2]]
    if n_min >= n_sum:
      save = i
      n_min = n_sum
  save = [num[save[0]], num[save[1]], num[save[2]]]
  save.sort()

  result = save[0] * (n ** 2 + (n - 1) ** 2 * 4)
  result += save[1] * ((n - 1) * 2) * 4
  result += save[2] * 4

  print(result)