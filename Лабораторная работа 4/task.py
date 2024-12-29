class Car:
    """
    Базовый класс для описания автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация общих атрибутов автомобиля.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """

        self._brand = brand  # Марка автомобиля (защищённый атрибут)
        self._model = model  # Модель автомобиля (защищённый атрибут)
        self._year = year  # Год выпуска (защищённый атрибут)

    @property
    def brand(self) -> str:
        """
        Возвращает год выпуска автомобиля.
        """
        return self._year

    @property
    def model(self) -> str:
        """
        Возвращает модель автомобиля.
        """
        return self._model

    @property
    def year(self) -> int:
        """
        Возвращает год выпуска автомобиля.
        """
        return self._year

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля для пользователя.
        """
        return f"Автомобиль {self._brand} {self._model}, {self._year} года выпуска"

    def __repr__(self) -> str:
        """
        Возвращает программное представление автомобиля.
        """
        return f"Car(brand='{self._brand}', model='{self._model}', year={self._year})"

    def start_engine(self) -> str:
        """
        Метод для запуска двигателя.
        """
        return f"Двигатель {self._brand} {self.model} запущен. 'RAAAAARRRR'"

    def stop_engine(self) -> str:
        """
        Метод для выключения двигателя.
        """
        return f"Двигатель {self._brand} {self.model} заглушен."

    def get_description(self) -> str:
        """
        Возвращает описание автомобиля.
        """
        return f"{self._brand} {self._model}, {self._year} года выпуска."


class FrontEngineCar(Car):
    """
    Класс для описания переднемоторного автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int, car_mileage: float):
        """
        Инициализация переднемоторного автомобиля.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param car_mileage: Пробег автомобиля
        """
        super().__init__(brand, model, year)  # FYc
        self.engine_position = "Переднемоторная компоновка"
        self.car_mileage = car_mileage

    def __str__(self) -> str:
        """
        Возвращает строковое представление переднемоторного автомобиля.
        """
        return f"{super().__str__()}. Расположение двигателя: {self.engine_position}, Пробег: {self.car_mileage}"

    def __repr__(self) -> str:
        """
        Возвращает программное представление переднемоторного автомобиля.
        """
        return f"FrontEngineCar(brand='{self._brand}', model='{self._model}', year={self._year}, engine_position='{self.engine_position}', car_mileage = {self.car_mileage}')"

    def start_engine(self) -> str:  # Наследование метода запуска двигателя
        return super().start_engine()

    def stop_engine(self) -> str:  # Наследование метода выключения двигателя
        return super().stop_engine()

    def get_description(self) -> str:  # Наследование и перегрузка описательного метода
        """
        Возвращает описание переднемоторного автомобиля.
        Перегрузка на случай "побеганного" автомобиля, требующего внимания
        """
        if self.car_mileage > 200000:
            return f"{super().get_description()} года выпуска - Переднемоторный автомобиль, нуждающийся в дополнительном обслуживании в силу большого пробега"
        else:
            return f"{super().get_description()} года выпуска - Переднемоторный автомобиль, пробег: {self.car_mileage}"


class RearEngineCar(Car):
    """
    Класс для описания заднемоторного автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int, engine_power: float):
        """
        Инициализация заднемоторного автомобиля.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param engine_power: Мощность двигателя
        """
        super().__init__(brand, model, year)
        self.engine_position = "Заднее расположение"
        self.engine_power = engine_power

    def __str__(self) -> str:
        """
        Возвращает строковое представление заднемоторного автомобиля.
        """
        return f"{super().__str__()}. Расположение двигателя: {self.engine_position}, Мощность: {self.engine_power}"

    def __repr__(self) -> str:
        """
        Возвращает программное представление заднемоторного автомобиля.
        """
        return f"RearEngineCar(brand='{self._brand}', model='{self._model}', year={self._year}, engine_position='{self.engine_position}', engine_power = {self.engine_power})"

    def start_engine(self) -> str:  # Наследование метода запуска двигателя
        return super().start_engine()

    def stop_engine(self) -> str:  # Наследование метода выключения двигателя
        return super().stop_engine()

    def get_description(self) -> str:# Наследование и перегрузка описательного метода
        """
        Возвращает описание заднемоторного автомобиля.
        Перегрузка на случай "веселого" на треке автомобиля
        """
        if self.engine_power > 360:
            return f"{super().get_description()} года выпуска - заднемоторный автомобиль, на котором стоит выехать на трек"
        else:
            return f"{super().get_description()} года выпуска - заднемоторный автомобиль, мощность: {self.engine_power}"
'''        
# Создание объектов
car1 = Car(brand="Toyota", model="Corolla", year=2020)
front_car = FrontEngineCar(brand="Honda", model="Civic", year=2018, car_mileage=150000)
rear_car = RearEngineCar(brand="Porsche", model="911", year=2021, engine_power=450)

# Демонстрация методов класса Car
print("Car1:")
print(car1)  # Строковое представление
print(repr(car1))  # Программное представление
print(car1.start_engine())  # Запуск двигателя
print(car1.stop_engine())  # Остановка двигателя
print(car1.get_description())  # Описание
print("\nFrontEngineCar:")
print(front_car)  # Строковое представление
print(repr(front_car))  # Программное представление
print(front_car.start_engine())  # Запуск двигателя
print(front_car.stop_engine())  # Остановка двигателя
print(front_car.get_description())  # Описание
print("\nRearEngineCar:")
print(rear_car)  # Строковое представление
print(repr(rear_car))  # Программное представление
print(rear_car.start_engine())  # Запуск двигателя
print(rear_car.stop_engine())  # Остановка двигателя
print(rear_car.get_description())  # Описание
'''