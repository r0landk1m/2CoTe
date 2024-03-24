test_case = int(input())

def rever(l):
  return l.reverse()

for _ in range(test_case):
  case = list(input())
  n = int(input())
  str = input()
  str = str[1:len(str) - 1]
  array = list(str.split(","))
  crite = 0
  for i in case:
    print(len(array))
    if len(array) == 0:
      crite = 1
      break
    if i == "R":
      array.reverse()
    else:
      del array[0]
  if crite == 1:
    print("error")
  else:
    print(array)