#Создать базовый класс сотрудник и два дочерних класса – менеджер и работник.
#В базовый класс добавить get_paid(), который в дальнейшем переопределить в дочерних,
#чтобы сотрудники разных должностей получали различную зарплату

class Employee:

    def get_paid(self):
        return self.salary + self.prize + self.sales


class Worker(Employee):
    def __init__(self, salary, prize, sales):
        self.salary = salary
        self.prize = prize
        self.sales = sales
        self.sales = 0

    def __str__(self):
        return Employee.get_paid


class Manager(Employee):

    def __init__(self, salary, prize, sales):
        self.salary = salary
        self.prize = prize
        self.sales = sales

    def __str__(self):
        return Employee.get_paid


anna = Manager(35000, 10000, 6000)
print(anna.get_paid())

sergey = Worker(50000, 20000, 0)
print(sergey.get_paid())

#рассмотреть наследование еще раз