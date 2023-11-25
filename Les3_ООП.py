from datetime import datetime

class From_birth_year:
    def __init__(self, name: str, birth_year: int) -> None:
        self.name = name
        self.age = datetime.now().year - birth_year

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    @classmethod
    def from_person_alt(cls, person_alt: From_birth_year) -> 'Person':
        return cls(person_alt.name, person_alt.age)
    
    def __str__(self) -> str:
        return f'Это {self.name}. Ему {self.age} лет.'
    
person1 = Person("Андрей", 25)
print(person1)

alt_data = From_birth_year("Константин", 1975)
person2 = Person.from_person_alt(alt_data)
print(person2)
