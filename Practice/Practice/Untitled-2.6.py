class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Woof")


class Cat(Animal):
    def sound(self):
        print("Meow")


class Cow(Animal):
    def sound(self):
        print("Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
