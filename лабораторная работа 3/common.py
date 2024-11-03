# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, con=","):
    group_1 = set(str1.split(con))
    group_2 = set(str2.split(con))
    group_com = sorted(list(group_1.intersection(group_2)))
    return group_com



participants_first_group = "Иванов|Петро|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, con="|")) #


