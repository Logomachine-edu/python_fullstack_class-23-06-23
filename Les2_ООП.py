from typing import Union

class Library:
    list_of_books = list()

    def add_book(self, book_title: str, book_author: str) -> str:
        self.book_title = book_title
        self.book_author = book_author
        self.add_book_to_list(self)
        print(f'Книга "{self.book_title}" добавлена')
        return Library()
    
    @classmethod
    def add_book_to_list(cls, book) -> str:
        cls.list_of_books.append(book)
        return
    
    def remove_book(self, title: str) -> str:
        for book in Library.list_of_books:
            if book.book_title == title:
                self.remove_book_from_list(book)
                print(f'Книга "{book.book_title}" удалена')
                return Library()
        print(f'Книги "{title}" нет в списке')
        return Library()

    @classmethod
    def remove_book_from_list(cls, book) -> str:
        cls.list_of_books.remove(book)
        return
        
    def __getitem__(self, index: Union[int, slice]) -> str:
        if isinstance(index, int):
            return f'"{Library.list_of_books[index].book_title}" - {Library.list_of_books[index].book_author}'
        elif isinstance(index, slice):
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else len(Library.list_of_books)
            step = index.step if index.step is not None else 1
            slice_list = [
                f'"{book.book_title}" - {book.book_author}'
                for book in Library.list_of_books[start:stop:step]
            ]
            return '; '.join(slice_list)
    
    def __contains__(self, title: str) -> bool:
        return title in [book.book_title for book in Library.list_of_books]
    

book1 = Library()
book2 = Library()
book3 = Library()
book4 = Library()
my_library = Library()
few_books = Library()
book1.add_book('Война и мир', 'Лев Толстой')
book2.add_book('Горе от ума', 'Александр Грибоедов')
book3.add_book('Ревизор', 'Николай Гоголь')
book4.add_book('Война и мир', 'Лев Толстой')

book2.remove_book('Горе от ума')
book2.remove_book('Мертвые души')

print(my_library[0])
print(my_library[1])
print(my_library[::])

print('Ревизор' in my_library)
print('Горе от ума' in my_library)
print('Война и мир' in my_library)

few_books.add_book('Мертвые души', 'Николай Гоголь').add_book('Муму', 'Иван Тургенев').remove_book('Ревизор')
print(my_library[::])
# print(Library())
# print(my_library.list_of_books)
# print(book1, book2, book3, book4, few_books)