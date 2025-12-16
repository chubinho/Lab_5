from src.book import Book,FictionBook, NonFictionBook


def test_default_book():
    book = Book("Хоббит", "Толкин", 1937, "Фэнтэзи", "isbn-456")
    assert book.title == "Хоббит"
    assert book.author == "Толкин"
    assert book.year == 1937
    assert book.genre == "Фэнтэзи"
    assert book.isbn == "isbn-456"


def test_fiction_book():
    book = FictionBook("Тарас Бульба", "Гоголь", 1834,
                       "Повесть", "isbn-199", 320)
    assert book.author == "Гоголь"
    assert book.title == "Тарас Бульба"
    assert book.year == 1834
    assert book.genre == "Повесть"
    assert book.pages == 320


def test_non_fiction_book_creation():
    book1 = NonFictionBook("Краткая история времени",
                           "Хокинг", 1988, "Научпоп", "isbn-789", 256)
    book2 = NonFictionBook("Геном", "Мэтт Ридли",
                           2020, "Научпоп", "isbn-978", 432)
    assert book1.title == "Краткая история времени"
    assert book1.pages == 256
    assert book2.pages == 432
    assert book2.isbn == "isbn-978"
