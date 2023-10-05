import unittest
from unittest.mock import patch, MagicMock


class Book:
    def __init__(self, id_book, title_book, author_book) -> None:
        self.id = id_book
        self.title = title_book
        self.author = author_book

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_author(self):
        return self.author

    def set_author(self, new_author):
        self.author = new_author

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def __str__(self) -> str:
        return f'Id({self.get_id()}), Author: {self.get_author()}, Title: {self.get_title()}'


class BookRepository:
    def __init__(self) -> None:
        self.rep = dict()

    def find_by_id(self, id_book: str):
        pass

    def find_all(self):
        return "res"


class BookService:
    def __init__(self) -> None:
        self.book_rep: BookRepository = BookRepository()

    def find_book_by_id(self, id_book):
        return self.book_rep.find_by_id(id_book)

    def find_all_books(self):
        return self.book_rep.find_all()


class InMemoryBookRepository(BookRepository):
    def __init__(self) -> None:
        super().__init__()
        self.rep['1'] = Book('1', 'test_title1', 'test_author1')
        self.rep['2'] = Book('2', 'test_title2', 'test_author2')

    def find_by_id(self, id_book: str):
        return self.rep[id_book]

    def find_all(self):
        return "\n".join(map(str, self.rep.values()))


class TestBookService(unittest.TestCase):
    
    def test_find_all_books(self):
        def mock_find_all(self):
            return 'Id(1), Author: test_author1, Title: test_title1\nId(2), Author: test_author2, Title: test_title2'
        patch('book.BookRepository.find_all', mock_find_all)
        result = BookService().find_all_books()
        expected = 'Id(1), Author: test_author1, Title: test_title1\nId(2), Author: test_author2, Title: test_title2'
        self.assertEqual(result, expected)

    def test_id_book(self):
        def mock_find_id(self, book_id):
            return 'Id(1), Author: test_author1, Title: test_title1'
        patch('book.BookRepository.find_by_id', mock_find_id)
        result = BookService().find_book_by_id('1')
        expected = 'Id(1), Author: test_author1, Title: test_title1'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
