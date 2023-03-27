class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speaks")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        
    def agee(self):
        print(f"{self.name} is {self.age} year old now ")

class Persia(Cat):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"{self.name} is a {self.color} persia that talks")

persia = Persia("Mocha", 1, "white")
persia.speak() # Output: Mocha is a white persia that talks
persia.agee() # Output: Mocha is 1 year old now