import pytest
from main import BooksCollector

class TestBooksCollector():
    @pytest.mark.parametrize('name', ['Я', 'Я+', 'Загадочная история Бенджамина Баттона..', 'Гордость и предубеждение и зомби и редис'])

    # тестируем add_new_book - добавление новой книги
    def test_add_new_book_if_add_2_book_true(self):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    # тестируем add_new_book - добавление книги дважды
    def test_add_new_book_twice_false(self):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    # тестируем get_book_genre - у добавленной книги нет жанра
     def test_get_book_genre_new_book_without_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    # тестируем set_book_genre - установление книге жанра
    def test_set_book_genre_book_has_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Комедии')
        assert collector.books_genre == {name: 'Комедии'}


    # тестируем get_books_with_specific_genre - выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_true():
        collector = BooksCollector()
        collector.add_new_book(name[0])
        collector.set_book_genre(name[0], 'Комедии')
        collector.add_new_book(name[1])
        collector.set_book_genre(name[1], 'Комедии')
        collector.add_new_book(name[2])
        collector.set_book_genre(name[2], 'Ужасы')
        assert collector.get_books_with_specific_genre('Комедии') == [name[0], name[1]]

    # тестируем get_books_for_children_true - возвращаем книги, подходящие детям
    def test_get_books_for_children_true():
        collector = BooksCollector()
        collector.add_new_book(name[0])
        collector.set_book_genre(name[0], 'Комедии')
        collector.add_new_book(name[1])
        collector.set_book_genre(name[1], 'Ужасы')
        assert collector.get_books_for_children() == [name[0]]


    # тестируем add_book_in_favorites - добавляем книгу в Избранное
    def test_add_book_in_favorites_true():
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]


    # тестируем delete_book_from_favorites - удаляем книгу из Избранного
    def test_delete_book_from_favorites_true():
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.get_list_of_favorites_books() != [name]


    # тестируем get_list_of_favorites_books - получаем список Избранных книг
    def test_get_list_of_favorites_books_true():
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books == [name]