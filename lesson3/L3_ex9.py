#Удалить все дубликаты из списка без использования дополнительных структур.
#Реализовать двумя видами циклов, для удаления можно использовать pop() либо del
list_a = ['a', 'b', 'c', 'd', 'a', 'e']
i = 0
j = 0
while i < len(list_a):
    j = i + 1
    while j < len(list_a):
        if list_a[i] == list_a[j]:
            list_a[j] = ''
            del list_a[j]
        else:
            j += 1
    i += 1
print(list_a)
