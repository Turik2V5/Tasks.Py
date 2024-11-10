# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as csv_file:
        data = [] # Будущий список словарей
        reader = csv.DictReader(csv_file)  # Используем DictReader для работы со строками как со словарями
        for row in reader:
            data.append(row)

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME,'w') as json_file:
        json.dump(data, json_file, indent=4)  #Перевод в JSON формат с отступом 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
