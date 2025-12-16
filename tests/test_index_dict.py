from src.index_dict import IndexDict
from src.book import FictionBook, NonFictionBook
import pytest


def test_index_dict_add_book():
    idx1 = IndexDict()
    book1 = FictionBook("1984", "Оруэлл", 1949, "Дистопия", "isbn-123", 328)
    idx1.add_book(book1)

    assert idx1["isbn-123"] == book1
    assert book1 in idx1["Оруэлл"]
    assert book1 in idx1[1949]

    idx2 = IndexDict()
    book2 = NonFictionBook("Краткая история времени",
                           "Хокинг", 1988, "Научпоп", "isbn-789", 256)
    idx2.add_book(book2)

    assert idx2["isbn-789"] == book2
    assert book2 in idx2["Хокинг"]
    assert book2 in idx2[1988]


def test_index_dict_remove_book():
    idx = IndexDict()
    book = FictionBook("1984", "Оруэлл", 1949, "Дистопия", "isbn-123", 328)
    idx.add_book(book)
    idx.remove_book(book)

    with pytest.raises(KeyError, match="Данные по переданному ключу не найдены"):
        idx["isbn-123"]

    with pytest.raises(KeyError, match="Данные по переданному ключу не найдены"):
        idx["Оруэлл"]

    with pytest.raises(KeyError, match="Данные по переданному ключу не найдены"):
        idx[1949]


def test_index_dict_contains():
    idx = IndexDict()
    book = FictionBook("Хоббит", "Толкин", 1937, "Фэнтэзи", "isbn-456",320)
    idx.add_book(book)
    assert "isbn-456" in idx
    assert book in idx["Толкин"]


def test_index_dict_keyerror():
    idx = IndexDict()
    with pytest.raises(KeyError,match="Данные по переданному ключу не найдены"):
        idx["несуществующий"]
    with pytest.raises(KeyError,match="Передан неверный ключ"):
        idx[*()]
