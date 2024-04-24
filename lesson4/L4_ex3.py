#Создать класс калькулятор и описать в нём методы для базовых математических операций для двух чисел

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def s_sum(self):
        return self.a + self.b

    def diff(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        if self.b > 0:
            return self.a / self.b
        else:
            print('Error')


p1 = Calculator(6, 3)
print(p1.s_sum())
print(p1.diff())
print(p1.mult())
print(p1.div())
