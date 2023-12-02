class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(degree: float) -> float:
        return degree * 1.8 + 32
    
    @staticmethod
    def fahrenheit_to_celsius(degree: float) -> float:
        return 5 / 9 * (degree - 32)
    
print(Temperature.celsius_to_fahrenheit(21.6))
print(Temperature.fahrenheit_to_celsius(168.1))
print(Temperature.celsius_to_fahrenheit(-5))
print(Temperature.fahrenheit_to_celsius(-35.1))