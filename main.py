test_case = int(input())
  
for _ in range(test_case):
  case = list(input())
  count_R = case.count("R")
  count_D = case.count("D")
  count_R %= 2
  n = int(input())
  str = input()
  str = str[1:len(str) - 1]
  array = str.split(",")

  if count_D <= n - 1:
    if count_R == 1:
      array.reverse()
    print(array[count_D:])
  else:
    print("error")