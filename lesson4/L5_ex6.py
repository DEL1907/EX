#Изучить что такое множественное наследование и миксины, привести пример
#использования данных концепций ООП

class Animal:

    def __init__(self, name, age, v):
        self.name = name
        self.age = age
        self.v = v


class Cage:
    cage = 0

    def __init__(self, cage1):
        self.cage += 1
        self.cage1 = cage1

    def save_cage_number(self):
        print(f"Живет в клетке: {self.cage}")


class Cats(Animal, Cage):
    def print_i(self):
        print(f"Name = {self.name}, Age = {self.age}, V = {self.v}, Num cage = {self.cage}")


tiger = Cats('Lina', 10, 'тигр')
tiger.print_i()
