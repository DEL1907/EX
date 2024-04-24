#Создать класс “Человек” с полями: имя, город проживания и год рождения.
#Написать метод, который будет возвращать возраст человека в годах


class People:
    def __init__(self, name, city, birth):
        self.name = name
        self.city = city
        self.birth = birth
        print("Человек по имени", self.name, "проживет в городе", city, "рожден в ", birth)

    def age(self):
        return 2024 - self.birth


p1 = People("Andrew", "Ufa", 1997)
print(p1.age())
