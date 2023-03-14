class Fahrenheit:
    def __init__(self, fahrenheit):
        self.f = fahrenheit

    def celcius(self):
        return (self.f - 32)*5/9 
    
    def kelvin(self):
        return (self.f + 459.67)*5/9
    
    def reamur(self):
        return 4/9*(self.f-32)
    
fahrenheitA = Fahrenheit(75)
print(f"Celcius: {fahrenheitA.celcius()}")
fahrenheitA = Fahrenheit(60)
print(f"Kelvin: {fahrenheitA.kelvin()}")
fahrenheitA = Fahrenheit(90)
print(f"Reamur: {fahrenheitA.reamur()}")