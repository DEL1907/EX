list_a = [1, 3, 5, 6]
list_b = [2, 4, 6, 7]
list_c = list_a + list_b
list_c.sort()
print(list_c)
list_res = list(set(list_c))
print(list_res)
