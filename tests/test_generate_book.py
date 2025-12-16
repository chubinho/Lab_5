from src.simulation import generate_book
from src.book import FictionBook, NonFictionBook

def test_generate_book_returns_book():
    book = generate_book()
    assert hasattr(book, "title")
    assert hasattr(book, "author")
    assert hasattr(book, "year")
    assert hasattr(book, "genre")
    assert hasattr(book, "isbn")
    assert hasattr(book, "pages")
    assert isinstance(book.isbn, str)
    assert isinstance(book.pages, int)
    assert book.pages > 0
    assert isinstance(book, (FictionBook, NonFictionBook))
