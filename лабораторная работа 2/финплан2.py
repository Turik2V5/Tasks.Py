salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
gap = spend - salary
for i in range(months - 1):
    spend += spend*increase
    gap += spend - salary
money_capital = int(gap)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")
