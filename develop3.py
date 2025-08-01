import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    """Фикстура для создания экземпляра BooksCollector"""
    return BooksCollector()

# 1. Тест для add_new_book (параметризованный)
@pytest.mark.parametrize('name, expected', [
    ('Властелин колец', True),    # валидное название
    ('', False),                  # пустая строка
    ('A'*41, False),              # слишком длинное название
    ('1984', True)                # граничный случай (4 символа)
])
def test_add_new_book(collector, name, expected):
    """Проверка добавления книги с разными названиями"""
    collector.add_new_book(name)
    assert (name in collector.get_books_genre()) == expected

# 2. Тест для set_book_genre
def test_set_book_genre(collector):
    """Проверка установки жанра для существующей книги"""
    collector.add_new_book('Метро 2033')
    collector.set_book_genre('Метро 2033', 'Фантастика')
    assert collector.get_book_genre('Метро 2033') == 'Фантастика'

# 3. Тест для get_book_genre
def test_get_book_genre(collector):
    """Проверка получения жанра по умолчанию"""
    collector.add_new_book('Книга без жанра')
    assert collector.get_book_genre('Книга без жанра') == ''

# 4. Тест для get_books_with_specific_genre
def test_get_books_with_specific_genre(collector):
    """Проверка фильтрации книг по жанру"""
    collector.add_new_book('Дюна')
    collector.set_book_genre('Дюна', 'Фантастика')
    assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

# 5. Тест для get_books_genre
def test_get_books_genre(collector):
    """Проверка получения словаря книг"""
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    assert len(collector.get_books_genre()) == 2

# 6. Тест для get_books_for_children
def test_get_books_for_children(collector):
    """Проверка получения детских книг"""
    collector.add_new_book('Малыш и Карлсон')
    collector.set_book_genre('Малыш и Карлсон', 'Мультфильмы')
    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')
    assert 'Малыш и Карлсон' in collector.get_books_for_children()
    assert 'Оно' not in collector.get_books_for_children()

# 7. Тест для add_book_in_favorites
def test_add_book_in_favorites(collector):
    """Проверка добавления в избранное"""
    collector.add_new_book('Шерлок Холмс')
    collector.add_book_in_favorites('Шерлок Холмс')
    assert 'Шерлок Холмс' in collector.get_list_of_favorites_books()

# 8. Тест для delete_book_from_favorites
def test_delete_book_from_favorites(collector):
    """Проверка удаления из избранного"""
    collector.add_new_book('Война и мир')
    collector.add_book_in_favorites('Война и мир')
    collector.delete_book_from_favorites('Война и мир')
    assert 'Война и мир' not in collector.get_list_of_favorites_books()

# 9. Тест для get_list_of_favorites_books
def test_get_list_of_favorites_books(collector):
    """Проверка получения списка избранных книг"""
    collector.add_new_book('Книга 1')
    collector.add_book_in_favorites('Книга 1')
    assert collector.get_list_of_favorites_books() == ['Книга 1']

# 10. Дополнительный тест (проверка добавления двух книг)
def test_add_two_books(collector):
    """Проверка добавления двух книг"""
    collector.add_new_book('Гордость и предубеждение')
    collector.add_new_book('Мастер и Маргарита')
    assert len(collector.get_books_genre()) == 2


