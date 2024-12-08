import doctest
# TODO: Подробно описать три произвольных класса
# TODO: описать класс
class Car:
    def __init__(self, brand: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Машина".

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля

        :raise ValueError: Если год выпуска меньше 1886 (года изобретения автомобиля).

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)  # инициализация экземпляра класса
        """
        if year < 1886:
            raise ValueError("Год выпуска должен быть не меньше 1886")

        self.brand = brand
        self.model = model
        self.year = year

    def get_age(self) -> int:
        """
        Получение возраста автомобиля.

        :return: Возраст автомобиля

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.get_age()
        4
        """
        return 2024 - self.year

    def update_model(self, new_model: str) -> None:
        """
        Обновление модели автомобиля.

        :param new_model: Новая модель автомобиля

        :raise ValueError: Если новая модель автомобиля является пустой строкой.

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.update_model("Corolla")
        >>> car.model
        'Corolla'
        """
        if not new_model:
            raise ValueError("Модель не должна быть пустой строкой")
        self.model = new_model
# TODO: описать ещё класс
class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга".

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        :raise ValueError: Если количество страниц отрицательное или равно нулю.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)  # инициализация экземпляра класса
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int) -> str:
        """
        Чтение книги.
        :param pages_read: Количество страниц, которые были прочитаны

        :raise ValueError: Если количество прочитанных страниц больше количества страниц в книге.

        :return: Статус чтения книги.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read(50)
        'Вы прочитали 50 страниц этого произведения.'
        """
        if pages_read > self.pages:
            raise ValueError("Вы не можете прочитать больше страниц, чем в книге")
        return f'Вы прочитали {pages_read} страниц этого произведения.'

    def get_author(self) -> str:
        """
        Получение автора книги.
        :return: Автор книги

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_author()
        'George Orwell'
        """
        return self.author


# TODO: и ещё один
class Tree:
    def __init__(self, species: str, age: int):
        """
        Создание и подготовка к работе объекта "Дерево".

        :param species: Вид дерева
        :param age: Возраст дерева в годах

        :raise ValueError: Если возраст меньше 0.

        Примеры:
        >>> oak = Tree("Oak", 10)  # инициализация экземпляра класса
        """
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным")

        self.species = species
        self.age = age

    def grow(self, years: int = 1) -> None:
        """
        Увеличение возраста дерева.

        :param years: Количество лет, на которое увеличивается возраст (по умолчанию 1)

        :raise ValueError: Если количество лет отрицательное.

        Примеры:
        >>> oak = Tree("Oak", 10)
        >>> oak.grow(5)
        >>> oak.age
        15
        """
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным")
        self.age += years

    def get_species(self) -> str:
        """
        Получение вида дерева.

        :return: Вид дерева

        Примеры:
        >>> oak = Tree("Oak", 10)
        >>> oak.get_species()
        'Oak'
        """
        return self.species