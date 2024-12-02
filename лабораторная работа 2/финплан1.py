money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
current = money_capital + salary - spend
count = 1
while current > 0:
    spend += spend * increase
    current += salary
    current -= spend
    count += 1

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", count - 1)
# в выводе -1 потому что цикл проверяет условие на следующей итерации а не на текущей
