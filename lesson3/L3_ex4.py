#Вывести каждый 3 элемент списка вместе с его индексом, используя enumerate()
list_a = input('Введите элементы списка: ')
list_b = ''
for i in enumerate(list_a):
    if i[0] % 3 == 0 and i[0] != 0:
        print(i[0], i[1])

