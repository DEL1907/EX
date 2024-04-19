#Расчет факториала числа с выводом каждого шага
k = 1
N = int(input('Введите число: '))
if N > 0:
    for i in range(1, N+1):
        k = k * i
        print(k)

