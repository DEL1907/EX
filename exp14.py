print('Транспонирование списка')
array = [[11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [41, 42, 43, 44, 45], [51, 52, 53, 54, 55]]
array_out = []
for i in range(len(array)):
    array_2 = []
    for item in array:
        array_2.append(item[i])
    array_out.append(array_2)
print(array_out)
