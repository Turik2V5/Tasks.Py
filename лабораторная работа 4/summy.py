import json
def task() -> float:
    with open('input.json', 'r') as file: # Чтение данных из JSON файла
        data = json.load(file)
    total_sum = 0
    for entry in data:
        total_sum += entry['score'] * entry['weight']
    return round(total_sum, 3)


print(task())