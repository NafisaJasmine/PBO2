class Reamur:
    def __init__(self, reamur):
        self.r = reamur

    def celcius(self):
        return self.r/0.8
   
    def fahrenheit(self):
        return (self.r*2.25)+32
    
    def kelvin(self):
        return (self.r/0.8)+273.15
    
reamurA = Reamur(75)
print(f"Celcius: {reamurA.celcius()}")
reamurA = Reamur(60)
print(f"Fahrenheit: {reamurA.fahrenheit()}")
reamurA = Reamur(90)
print(f"Kelvin: {reamurA.kelvin()}")