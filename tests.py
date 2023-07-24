import pytest
from main import BooksCollector

class TestBooksCollector():

    def test_add_new_book_if_add_2_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_twice_false(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        assert len(collector.get_books_genre()) == 1

    def test_get_book_genre_new_book_without_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        assert collector.get_book_genre('Загадочная история Бенджамина Баттона') == ''

    def test_set_book_genre_book_has_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        collector.set_book_genre('Загадочная история Бенджамина Баттона', 'Комедии')
        assert collector.get_book_genre('Загадочная история Бенджамина Баттона') == 'Комедии'

    def test_get_books_with_specific_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        collector.set_book_genre('Загадочная история Бенджамина Баттона', 'Комедии')
        collector.add_new_book('Утка')
        collector.set_book_genre('Утка', 'Комедии')
        collector.add_new_book('Мать')
        collector.set_book_genre('Мать', 'Ужасы')
        assert collector.get_books_with_specific_genre('Комедии') == ['Загадочная история Бенджамина Баттона', 'Утка']


    def test_get_books_with_specific_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        collector.set_book_genre('Загадочная история Бенджамина Баттона', 'Комедии')
        collector.add_new_book('Гуффи')
        collector.set_book_genre('Гуффи', 'Комедии')
        collector.add_new_book('Мать')
        collector.set_book_genre('Мать', 'Ужасы')
        assert collector.get_books_with_specific_genre('Комедии') == ['Загадочная история Бенджамина Баттона', 'Гуффи']

    def test_get_books_for_children_true(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        collector.set_book_genre('Загадочная история Бенджамина Баттона', 'Комедии')
        collector.add_new_book('Мать')
        collector.set_book_genre('Мать', 'Ужасы')
        assert collector.get_books_for_children() == ['Загадочная история Бенджамина Баттона']


    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        collector.add_book_in_favorites('Загадочная история Бенджамина Баттона')
        assert collector.get_list_of_favorites_books() == ['Загадочная история Бенджамина Баттона']


    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        collector.add_book_in_favorites('Загадочная история Бенджамина Баттона')
        collector.delete_book_from_favorites('Загадочная история Бенджамина Баттона')
        assert collector.get_list_of_favorites_books() != ['Загадочная история Бенджамина Баттона']


    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Загадочная история Бенджамина Баттона')
        collector.add_book_in_favorites('Загадочная история Бенджамина Баттона')
        assert collector.get_list_of_favorites_books() == ['Загадочная история Бенджамина Баттона']
    #