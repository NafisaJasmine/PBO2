class Kelvin:
    def __init__(self, kelvin):
        self.k = kelvin

    def celcius(self):
        return self.k - 273.15
    
    def fahrenheit(self):
        return (self.k * 9/5) - 459.67
    
    def reamur(self):
        return 4/5*(self.k - 273)
    
kelvinA = Kelvin(75)
print(f"Celcius: {kelvinA.celcius()}")
kelvinA = Kelvin(60)
print(f"Fahrenheit: {kelvinA.fahrenheit()}")
kelvinA = Kelvin(90)
print(f"Reamur: {kelvinA.reamur()}")