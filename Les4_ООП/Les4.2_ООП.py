class Greenhouse:
    def __init__(self, temperature: float, humidity: float, light_level: float) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__light_level = light_level
    
    @property
    def temperature(self) -> float:
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value: float) -> None:
        if value < 15 or value >30:
            raise ValueError("Температура в недопустимом диапазоне!")
        self.__temperature = value

    @property
    def humidity(self) -> float:
        return self.__humidity
    
    @humidity.setter
    def humidity(self, value: float) -> None:
        if value < 0 or value > 100:
            raise ValueError("Влажность в недопустимом диапазоне!")
        self.__humidity = value

    @property
    def light_level(self) -> float:
        return self.__light_level
    
    @light_level.setter
    def light_level(self, value: float) -> None:
        if value < 0 or value > 10_000:
            raise ValueError("Уровень света в недопустимом диапазоне!")
        self.__light_level = value

greenhouse = Greenhouse(20, 60, 1000)
print(greenhouse.temperature)
print(greenhouse.humidity)
print(greenhouse.light_level)

greenhouse.temperature = 29
print(greenhouse.temperature)
greenhouse.humidity = 31
print(greenhouse.humidity)
greenhouse.light_level = 6000
print(greenhouse.light_level)

# greenhouse.temperature = 70
# print(greenhouse.temperature)
# greenhouse.humidity = 200
# print(greenhouse.humidity)
# greenhouse.light_level = 16000
# print(greenhouse.light_level)

