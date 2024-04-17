string_a = input('Введите фамилию имя и отчество: ')
print(string_a)
a = string_a.split(' ')
string_name = a[1]
string_firstname = a[2]
print(a[0] + ' ' + string_name[0] + '.' + string_firstname[0] + '.')
