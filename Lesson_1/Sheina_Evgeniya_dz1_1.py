#duration = int(input())
#d = duration // 86400
#h = (duration - d * 86400) // 3600
#m = (duration - d * 86400 - h * 3600) // 60
#s = duration % 60
#print(d, 'дн', h, 'час', m, 'мин', s, 'сек')

# второй вариант
duration = int(input())
d = duration // 86400
h = (duration - d * 86400) // 3600
m = (duration - d * 86400 - h * 3600) // 60
s = duration % 60
if duration < 60:
    print(s, 'сек')
elif 60 <= duration < 360:
    print(m, 'мин', s, 'сек')
elif 360 <= duration < 86400:
    print(h, 'час', m, 'мин', s, 'сек')
else:
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
