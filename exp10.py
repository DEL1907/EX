from random import random
a = 10
list_a = [0] * a
for i in range(a):
    list_a[i] = int(random() * 50)
print(list_a)
for i in range(a-1):
    for j in range(i + 1, a):
        if list_a[i] == list_a[j]:
            print("Есть одинаковые")
    print("Все элементы уникальны")