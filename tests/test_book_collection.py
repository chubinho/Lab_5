from src.book_collection import BookCollection


def test_book_collection_getitem():
    books = BookCollection()
    b1 = ("Тарас Бульба", "Гоголь", 1834,
          "Повесть", "isbn-199", 320)
    b2 = ("Хоббит", "Толкин", 1937, "Фэнтэзи", "isbn-456")
    b3 = ("Краткая история времени",
          "Хокинг", 1988, "Научпоп", "isbn-789", 256)
    books.append(b1)
    books.append(b2)
    books.append(b3)
    assert books[0] == b1
    assert books[:2] == [b1, b2]


def test_book_collection_len():
    books = BookCollection()
    b1 = ("Хоббит", "Толкин", 1937, "Фэнтэзи", "isbn-456")
    b2 = ("Алые паруса", "Грин", 1916, "Повесть", "isbn-5131")
    books.append(b1)
    books.append(b2)
    assert len(books) == 2


def test_book_collection_iter():
    books = BookCollection()
    b1 = ("Хоббит", "Толкин", 1937, "Фэнтэзи", "isbn-456")
    b2 = ("Алые паруса", "Грин", 1916, "Повесть", "isbn-5131")
    arr = [b1, b2]
    for book in arr:
        books.append(book)
    assert len(books) == 2


def test_book_delitem():
    books = BookCollection()
    b1 = ("Хоббит", "Толкин", 1937, "Фэнтэзи", "isbn-456")
    b2 = ("Краткая история времени",
          "Хокинг", 1988, "Научпоп", "isbn-789", 256)
    books.insert(0, b1)
    books.append(b2)
    del books[0]
    assert books[0] == b2

def test_book_contains():
    books = BookCollection()
    b1 = ("Тарас Бульба", "Гоголь", 1834,
          "Повесть", "isbn-199", 320)
    b2 = ("Хоббит", "Толкин", 1937, "Фэнтэзи", "isbn-456")
    b3 = ("Краткая история времени",
          "Хокинг", 1988, "Научпоп", "isbn-789", 256)
    arr = [b1,b2,b3]
    for book in arr:
        books.append(book)
    assert b1 in books
    assert b2 in books
    assert b3 in books
