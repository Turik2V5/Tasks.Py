# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, con=","):
    group_1 = set(str1.split(con))
    group_2 = set(str2.split(con))
    group_com = sorted(list(group_1.intersection(group_2)))
    '''
    1)В строке 6 полсе применения intersection() действительно применяется сортировка, так как этого требует условие задания: 
    3.Верните полученный результат в виде списка общих участников отсортированных в алфавитном порядке
    2)А также, потому что intersection() не сортирует, что можно проверить на алфавитном порядке для примера, приведенного в выданном материале:
    set_ = {'c', 'a', 'z', 'b', 'r', 'q', 'q'}
    list_ = ['d', 'u', 'u', 'c', 'c', 'a', 'z', 'b']
    intersection_set = set_.intersection(list_)
    print(intersection_set)  # {'b', 'z', 'a', 'c'}
    3)Для конктреного текста из условия сортировка не нужна - он и так будет пройден, так как совпадение всего одно, но такое решение не будетт соответсвовать условию.
    4)В данном случае, при создании переменной и при работе с фамилиями, и при условии возвращения списка, удобно воспользоваться sorted.
    '''
    return group_com



participants_first_group = "Иванов|Петро|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, con="|")) #


