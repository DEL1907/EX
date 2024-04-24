#Создать класс для геометрической фигуры на выбор и добавить в него два метода
# – первый для расчета площади, второй для расчета периметра
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

    def perimeter(self):
        return self.radius * 2 * math.pi


r = Circle(5)
s = r.area()
p = r.perimeter()
print("Площадь круга = ", int(s), '\nПериметр = ', int(p))
