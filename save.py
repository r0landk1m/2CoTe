'''
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end:
    return

  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while start < right and array[right] >= array[pivot]:
      right -= 1

    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]

  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
'''



#8진수 출력
a = 0O177
print(a)
a = 127 (1 * 8**2 + 7 * 8 + 7)

#16진수 출력
b = 0x8ff
b = 0x8ABC
print(b)
b = 2748 (10 * 16**2 + 11 * 16 + 12)


# 문자열 속 따옴표 표시
'''
Food = "Python's favorite food is perl"
Say = '"python is very easy." he says.'
'''

food = "python's favorite food is perl"
print(food)

Say = '"python is very easy." he says.'
print(Say)

food = 'python\'s favorite food is perl'
Say = "\"python is very easy.\" he says."
print(food)
print(Say)

#여러줄인 문자열을 변수에 대입
"""
Life is too short
You need python
"""

multiline = "Life is too short \n You need python"
print(multiline)

multiline = '''
   life is too short
   you need python
   '''
print(multiline)
