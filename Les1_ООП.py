class Animal:
    def __init__(self, animal_name: str, animal_sound: str) -> None:
        self.animal_name = animal_name
        self.animal_sound = animal_sound

    def sounds(self) -> str:
        self.repeat_sounds = '-'.join(list([self.animal_sound for i in range(3)]))
        return f'{self.repeat_sounds}'
    
    def eating(self) -> str:
        return f'{self.animal_name} кушает'

cat = Animal('Кошка', 'Мяу')
dog = Animal('Собака', 'Гав')
cow = Animal('Корова', 'Муу')

print(cat.sounds())
print(cat.eating())
print(dog.sounds())
print(dog.eating())
print(cow.sounds())
print(cow.eating())