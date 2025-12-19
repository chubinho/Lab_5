### Ошибка 5 - перепутанны поля объекта  

### Место: book.py, класс Book и наследуемые от него классы
### Симптом:
Неправильное отображение книг: в Book в поле title хранится автор, в поле author - название книги, в поле genre - год создания книги, в поле year - жанр. А наследуемые классы  FictionBook и NonFictionBook передают в родительский конструктор genre как title, author как author(но это уже жанр), title как year и year как genre.

### Как воспроизвести:
Запустить  `python .\src\simulation.py 20 11`

### Откладка: 
Установлены breakpoints на строках вовзращаемых строк в магическом методе `__repr__` в классах Book, FinctionBook и NonFictionBook.

### Причина:
В конструкторах класса Book и наследуемых классах FInctionBook и NonFictionBook перепутаны аргументы при присваивании значений полям объекта.

### Исправление:
Каждому полю объекта подобрать правильное значение
```
class Book:
    """Создание базового класса"""
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self) -> str:
        """
        Вывод определенных атрибутов класса
        """
        return f'Произведение "{self.title}", написанное автором {self.author} в {self.year}'
```

### Проверка:
Поведение симуляции соответствует ожидаемому: каждое поле объекта имеет корректное значение.

### Доказательства:
Вывод проблемы:
![!\[alt text\](image-24.png)](report_png/5-1.png)

![!\[alt text\](image-31.png)](report_png/5-2.png)

![report_png/5-3.pnп](report_png/5-3.png)


Код исправления:
![!\[alt text\](image-25.png)](report_png/5-4.png)


