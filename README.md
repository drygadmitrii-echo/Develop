# Тестирование класса BooksCollector

## Реализованные тесты

1. `test_add_new_book` - проверка добавления книг с разными названиями (параметризованный)
2. `test_set_book_genre` - проверка установки жанра
3. `test_get_book_genre` - проверка получения жанра по умолчанию
4. `test_get_books_with_specific_genre` - проверка фильтрации по жанру
5. `test_get_books_genre` - проверка получения словаря книг
6. `test_get_books_for_children` - проверка получения детских книг
7. `test_add_book_in_favorites` - проверка добавления в избранное
8. `test_delete_book_from_favorites` - проверка удаления из избранного
9. `test_get_list_of_favorites_books` - проверка получения списка избранного
10. `test_add_two_books` - проверка добавления нескольких книг

## Запуск тестов

```bash
pytest -v tests.py
