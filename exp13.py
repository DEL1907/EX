students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

print('Всех: ')
print(students, employees)
print(students.union(employees))

print('Всех тех, кто одновременно учится и работает: ')
print(students.intersection(employees))
print(students & employees)

print('Всех тех, кто только работает, но не учится: ')
print(employees.difference(students))
print(employees - students)

print('Всех тех, кто либо учится, либо работает, но не одновременно: ')
print(students.symmetric_difference(employees))
print((employees - students) | (students - employees))
