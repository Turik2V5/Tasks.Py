numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
missed = numbers.index(None)
shortlist = numbers[:missed] + numbers[missed+1:]
newelem = sum(shortlist) / len(numbers)
numbers[missed] = newelem

print("Измененный список:", numbers)
