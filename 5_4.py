def f(team):
    group_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    group_2 = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    for i in range(5):
        team.append(group_1[i+1])
    for i in range(5):
        team.append(group_2[i])
    return (*group_1, *group_2, *team, len(team), sorted(team), 'Иванов' in team)


print(f([]))