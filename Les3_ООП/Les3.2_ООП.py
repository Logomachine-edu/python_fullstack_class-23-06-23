from datetime import datetime

class Person:
    population: int = 0

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.population += 1
    
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
        return cls(name, datetime.now().year - birth_year)
    
    def __str__(self) -> str:
        return f'Это {self.name}. Ему {self.age}.'
    
    @classmethod
    def display_population(cls) -> None:
        print(f"Население - {cls.population} чел.")
    
person1 = Person("Андрей", 25)
print(person1)
person2 = Person.from_birth_year("Игорь", 1970)
print(person2)
person3 = Person("Олег", 14)
print(person3)

Person.display_population()