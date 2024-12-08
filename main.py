# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from task_1 import Car, Book, Tree

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.
    car = Car("Toyota", "Camry", 2020)
    book = Book("1984", "George Orwell", 328)
    oak = Tree("Oak", 10)

    try:
        # TODO: вызвать метод с некорректными аргументами(b)
        # Вызываем метод update_model с некорректным аргументом
        car.update_model("")  # Пытаемся установить пустую модель
    except ValueError:
        print('Ошибка: неправильные данные, модель не должна быть пустой строкой.')

    try:
        # TODO: вызвать метод с некорректными аргументами(a)
        # Вызываем метод read с некорректным аргументом
        book.read(400)  # Пытаемся прочитать больше страниц, чем в книге
    except ValueError:
        print('Ошибка: неправильные данные, вы не можете прочитать больше страниц, чем в книге.')

    try:
        # TODO: вызвать метод с некорректными аргументами(a)
        oak.grow(-2)  # Пытаемся увеличить возраст дерева на отрицательное число
    except ValueError:
        print('Ошибка: неправильные данные, количество лет не может быть отрицательным.')