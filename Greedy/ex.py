# 500원, 100원, 50원, 10원 동전 존재
# N(거스름 돈)은 항상 10의 배수

money = int(input())
N = money // 500
money %= 500
N += money // 100
money %= 100
N += money // 50
money %= 50
N += money // 10
print(N)

'''
money = int(input())
coin = [500, 100, 50, 10]
N = 0
for a in coin:
    N += money // a
    money %= a
print(N)
'''