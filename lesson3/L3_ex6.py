#Подсчитать количество цифр в числе. Реализовать двумя видами циклов
a = int(input())
k = 0
while a > 0:
    k = k + 1
    a = a // 10
print(k)

b = int(input('2: '))
n = 0
if a > 0:
    k = k + 1
    a = a // 10
print(k)