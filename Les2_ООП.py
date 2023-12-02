from typing import Union


class Library:  
    def __init__(self) -> None:
        self.list_of_books = list()

    def add_book(self, book_title: str, book_author: str) -> list[tuple[str, str]]:      
        self.list_of_books.append((book_title, book_author))
        print(f'Книга "{book_title}" добавлена')
        return self
    
    def remove_book(self, title: str) -> list[tuple[str, str]]:
        for book_i in self.list_of_books:
            if book_i[0] == title:
                self.list_of_books.remove(book_i)
                print(f'Книга "{title}" удалена')
                return self
        print(f'Книги "{title}" нет в списке')
        return self
        
    def __getitem__(self, index: Union[int, slice]) -> Union[tuple[str, str], list[tuple[str, str]]]:
        if isinstance(index, int):
            return self.list_of_books[index]
        elif isinstance(index, slice):
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else len(self.list_of_books)
            step = index.step if index.step is not None else 1
            return self.list_of_books[start:stop:step]
    
    def __contains__(self, title: str) -> bool:
        return title in [book[0] for book in self.list_of_books]
    
    def __str__(self) -> str:
        return ";\n".join([f'"{book[0]}" - {book[1]}' for book in self.list_of_books])
    
my_library = Library()
my_library.add_book('Война и мир', 'Лев Толстой')
my_library.add_book('Горе от ума', 'Александр Грибоедов')
my_library.add_book('Ревизор', 'Николай Гоголь')
my_library.add_book('Война и мир', 'Лев Толстой')

my_library.remove_book('Горе от ума')
my_library.remove_book('Мертвые души')

print(my_library[0])
print(my_library[1])
print(my_library[::])

print('Ревизор' in my_library)
print('Горе от ума' in my_library)
print('Война и мир' in my_library)

my_library.add_book('Мертвые души', 'Николай Гоголь').add_book('Муму', 'Иван Тургенев').remove_book('Ревизор')
print(my_library[::])
print(str(my_library))

