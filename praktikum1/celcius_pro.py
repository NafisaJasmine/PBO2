# Nama : Nafisa Nurul Jasmine
# NIM : 210511041
# Kelas : D

class Celcius:
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5
    
mycelcius = 75
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
print("konversi ",mycelcius, "derajat celcius adalah ",myfahrenheit, "derajat fahrenheit")
mycelcius = 60
mykelvin = Celcius.to_kelvin(mycelcius)
print ("konversi ",mycelcius, "derajat celcius adalah ",mykelvin, "derajat Kelvin")
mycelcius = 90
myreamur = Celcius.to_reamur(mycelcius)
print ("konversi ",mycelcius, "derajat celcius adalah ",myreamur, "derajat Reamur")