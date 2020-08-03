
# Object Oriented Programming in Python

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old")

    def speak(self):
        print("I dont know what I say")


class Cat(Pet):
    def speak(self):
        print("Meow!")


class Dog(Pet):
    def speak(self):
        print("Bark!")


p = Pet("Jim", 12)
c = Cat("Lana", 5)
d = Dog("Tom", 10)
print(p.name)
p.speak()
c.speak()
d.speak()
