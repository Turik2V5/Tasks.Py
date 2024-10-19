list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

first_team = []
second_team = []
for i in range(len(list_players)):
    if i <= ((len(list_players) / 2) - 1):
        first_team.append(list_players[i])
    else:
        second_team.append(list_players[i])

print(first_team)
print(second_team)
