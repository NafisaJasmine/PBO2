class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal speaks")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("The cat meow")


class Persia(Cat):
    def __init__(self, name, breed, origin):
        super().__init__(name, breed)
        self.origin = origin

    def speak(self):
        print("The persia snoring")

animal = Animal("Cat")
animal.speak() # output: The animal speaks

cat = Cat("Cat", "Persia")
cat.speak() # output: The cat meow

persia = Persia("Cat", "Persia", "Persia")
persia.speak() # output: The persia snoring