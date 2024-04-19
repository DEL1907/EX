#Вывести каждую букву строки в обратном порядке без использования reversed() или [::-1]
str_a = input(': ')
str_b = []
for i in range(len(str_a) - 1, -1, -1):
    str_b.append(str_a[i])
print(str_b)
