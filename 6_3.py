d = {
    'Ivanov': 'German Russian English Spanish Chinese',
    'Petrov': 'Russian Spanish',
    'Sidorov': ' Russian English Chinese'
}

s = set()
s1 = ''

for i in d:
    for j in d[i].split():
        s.add(j)
        if 'Chinese' == j:
            s1 += i
            s1 += ' '

print(len(s))
print(sorted(s))
print(s1.split())
