#Изучить метод  __str__, создать класс с данным методом, продемонстрировать его выполнение

class Time:
    def __init__(self, t):
        self.t = t

    def __str__(self):
        return self.t


t2 = Time('Summer')
print(t2)

class Time1:

    def __init__(self, t3):
        self.t3 = t3


t4 = Time1('Summer')
print(t4)
