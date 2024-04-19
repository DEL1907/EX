#Подсчет суммы всех четных чисел от 1 до n. Реализовать двумя видами циклов
N = int(input('Введите любое число: '))
N += 1
sum_2 = 0
k = 0
for k in range(int(N)):
    if k % 2 == 0:
        sum_2 = sum_2 + k
        k += 1
print(sum_2)

k = 0
sum_3 = 0
for k in range(int(N)):
    while (k % 2 == 0):
        sum_3 += k
        k += 1
print(sum_3)


