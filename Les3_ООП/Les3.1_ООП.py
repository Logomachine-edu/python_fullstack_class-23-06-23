from datetime import datetime

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
        return cls(name, datetime.now().year - birth_year)
    
    def __str__(self) -> str:
        return f'Это {self.name}. Ему {self.age}.'
    
person1 = Person("Андрей", 25)
print(person1)

person2 = Person.from_birth_year("Игорь", 1970)
print(person2)
