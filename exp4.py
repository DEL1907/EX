string_c = input('Введите строку')
kol_vo = 0
i = 0
for i in range(0, len(string_c)):
    if string_c[i] == ' ' or string_c[i] == ',' or string_c[i] == '.' or string_c[i] == '':
        kol_vo += 1
print (kol_vo+1)