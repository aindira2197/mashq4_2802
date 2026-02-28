class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "vov vov"


print(Dog("Bobik").speak())


class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Men {self.name}"


class Cat(Animal):
    pass


c = Cat("Mimi")
print(c.info())



class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, stack):
        super().__init__(name)
        self.stack = stack


dev = Developer("Alim", "python")
print(dev.name, dev.stack)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors


c = Car("BMW", 4)
print(c.brand, c.doors)

