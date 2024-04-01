'''print(print )
lst = list(map(int, input().split()))
if len(lst) != len(set(lst)):
    pass
d = dict()
n = int(input('Введите количество'))

keys = [i for i in range(int(input('Введите количество элементов списка: ')))]
values = [int(input('Введите элемент списка: ')) for _ in range(len(keys))]

d = {key: value for key, value in zip(keys, values)}
print(d)


#print({key: value for key, value in zip([i for i in range(int(input('Введите желаемое количество элементов: ')))], [int(input('Введите элемент списка: ')) for _ in range(int(input('Повторно введите желаемое количество элементов: ')))])}.values())
print(*[i := int(input('Введите элемент: ')) if i in s])
'''
from random import *

def f():
    lst = [randint(0, 100) for i in range(randint(5, 90))]
    if len(lst) != len(set(lst)):
        for i in lst:
            for j in range(i + 1, len(lst)):
                if i == lst[j]:
                    return i


print(f())
