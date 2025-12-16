from src.book import FictionBook, NonFictionBook
from src.library import Library


def test_library_add_book():
    lib = Library()
    book = FictionBook("Хоббит", "Толкин", 1937, "Фэнтэзи", "isbn-456", 320)
    lib.add_book(book)
    assert len(lib.books) == 1
    assert "isbn-456" in lib.index
    assert book in lib.index["Толкин"]


def test_library_remove_book():
    lib = Library()
    book1 = NonFictionBook("Краткая история времени",
                           "Хокинг", 1988, "Научпоп", "isbn-789", 256)
    book2 = NonFictionBook("Геном", "Мэтт Ридли",
                           2020, "Научпоп", "isbn-978", 432)
    lib.add_book(book1)
    lib.add_book(book2)
    lib.remove_book("isbn-789")
    assert len(lib.books) == 1
    assert len(lib.index) == 1


def test_library_find_by_author():
    lib = Library()
    book1 = FictionBook("Евгений Онегин", "Пушкин",
                        1833, "Роман", "isbn-222", 640)
    book2 = FictionBook("Капитанская дочка", "Пушкин",
                        1836, "Роман", "isbn-777", 168)
    lib.add_book(book1)
    lib.add_book(book2)
    found = lib.find_by_author("Пушкин")
    assert len(found) == 2
    assert book1 in found
    assert book2 in found


def test_library_find_by_isbn():
    lib = Library()
    book = NonFictionBook("Геном", "Мэтт Ридли",
                          2020, "Научпоп", "isbn-978", 432)
    lib.add_book(book)
    found = lib.find_by_isbn("isbn-978")
    assert found == book


def test_library_find_by_year():
    lib = Library()
    book = FictionBook("Тарас Бульба", "Гоголь", 1834,
                       "Повесть", "isbn-199", 320)
    lib.add_book(book)
    found = lib.find_by_year(1834)
    assert len(found) == 1
    assert book in found


def test_library_find_by_genre():
    lib = Library()
    book = FictionBook("Тарас Бульба", "Гоголь", 1834,
                       "Повесть", "isbn-199", 320)
    lib.add_book(book)
    found = lib.find_by_genre("Повесть")
    assert len(found) == 1
    assert book in found
