'''k = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
w = int(input('Сколько выходных хотите? '))
print(f'Будние дни: {k[:-w]} \nВыходные дни: {k[-w:]}')
'''
def f(k, w):
    return f'Будние дни: {k[:-w]} \nВыходные дни: {k[-w:]}'


print(f(['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'], int(input('Сколько выходных хотите? '))))