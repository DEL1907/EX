#Найти самое длинное слово из массива. Реализовать двумя видами циклов
arr_1 = ['i', 'like', 'jam', 'f']
arr_2 = 0
k = len(arr_1)
for i in range(0, len(arr_1)):
    if i < len(arr_1):
        if arr_1[i] > arr_1[i+1]:
            arr_2 = arr_1[i]
        else:
            arr_2 = arr_1[i]
print(arr_2)
#не работает надо заменить arr_1[i+1]: