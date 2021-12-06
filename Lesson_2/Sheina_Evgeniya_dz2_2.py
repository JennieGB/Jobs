word_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
wl = []
for i in word_list:
    if i.isdigit():
        wl.append(f'"{i:0>2}"')
    elif i[0] == '+':
        wl.append(f'"+{i[1:]:0>2}"')
    else:
        wl.append(i)
delimiter = ' '
output = delimiter.join(wl)
print(output)






