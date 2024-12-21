class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        # Перед name и author добавлены нижнее подчеркивая как для защищенных атрибутов не требующих проверок
        # Эти атрибуты нельзя изменять и они станут "read-only" через свойства
        self._name = name
        self._author = author

    # Свойство для name не позволяющее его изменять
    @property
    def name(self) -> str: #
        """Название книги (только для чтения)."""
        return self._name

    # Свойство для author не позволяющее его изменять
    @property
    def author(self) -> str:
        """Автор книги (только для чтения)."""
        return self._author

    def __str__(self):
        """Пользовательское строковое представление"""
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """Программное строковое представление"""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author) # Наследуем название и автора из базового класса
        self.pages = pages # Устанавливаем количество страниц как публичный атрибут для проведения проверки через свойства

    # Cвойство для количества страниц включающее getter и setter для проверки на целочисленность и положительность
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value # Сохраняем значение в защищенный атрибут
    # Так как вывод такой же как и в базовом классе, методы __str__ и __repr__ можно унаследовать из него
    # Также их можно перегрузить, добавим информацию о количестве страниц
    def __str__(self):
        return f"{super().__str__()}. Страниц: {self.pages}"

    def __repr__(self):
        return f"PaperBook({super().__repr__()}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # Наследуем название и автора из базового класса
        self.duration = duration # Устанавливаем продолжительность с проверкой

    # Свойство для продолжительности с проверкой на числовой тип и положительное значение.
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value  # Сохраняем значение в защищенный атрибут
    # Так как вывод такой же как и в базовом классе, методы __str__ и __repr__ можно унаследовать из него
    # Также их можно перегрузить, добавим информацию о продолжительности
    def __str__(self):
        return f"{super().__str__()}. Длительность: {self.duration}"

    def __repr__(self):  # __repr__ перегрузим для каждого дочернего класса
        return f"AudioBook({super().__repr__()}, duration={self.duration!r})"
