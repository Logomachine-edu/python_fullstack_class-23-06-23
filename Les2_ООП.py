class Library:
    def __init__(self) -> None:
        self.book_list = {}

    def add_book(self, title: str, author: str) -> str:
        self.book_list[title] = author
        print(f'Книга "{title}" добавлена')
        return self
    
    def remove_book(self, title: str) -> str:
        self.book_list.pop(title)
        print(f'Книга "{title}" удалена')
        return self

    def __getitem__(self, index: int) -> str:
        to_list = list(self.book_list)
        return to_list[index]
    
    def __contains__(self, title: str) -> bool:
        return title in self.book_list

my_library = Library()
my_library.add_book('Война и мир', 'Лев Толстой')
my_library.add_book('Горе от ума', 'Александр Грибоедов')
my_library.add_book('Ревизор', 'Николай Гоголь')
print(my_library.book_list)
my_library.remove_book('Горе от ума')
print(my_library.book_list)
print(my_library[0])
print(my_library[1])
print('Ревизор' in my_library)
print('Горе от ума' in my_library)
my_library.add_book('Мертвые души', 'Николай Гоголь').remove_book('Война и мир').add_book('Муму', 'Иван Тургенев')
print(my_library.book_list)


