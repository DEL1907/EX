#Проверить, является ли строка палиндромом (зеркальная)
str_a = input('введите строку для проверки на зеркальность: ')
if str_a == str_a[::-1]:
    print('строка является палиндромом')
else:
    print('строка не является палиндромом')
