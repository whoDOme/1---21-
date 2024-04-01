d = {
    'Russia': 'Moscow',
    'USA': 'Washington',
    'Belarus': 'Minsk'
}

for i in d:
    print(i, d[i])

print(d[input('Введите страну: столица которой нужна: ')])

for i in sorted(d):
    print(i)