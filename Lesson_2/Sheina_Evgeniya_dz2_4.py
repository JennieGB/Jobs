lst = [100.25, 346, 234.5, 500, 471.25, 199.45, 150, 297, 355, 342.5, 234.51]
lst1 = []
for price in lst:
    rub = int(price)
    kop = (price - int(price)) * 100
    lst1.append(f'{rub} руб. {kop:02.0f} коп.')
delimiter = ', '
output = delimiter.join(lst1)
print(output)
lst1_copy = lst1
lst1_copy.sort()
print(lst1)
print(id(lst1) == id(lst1_copy))
print(lst1_copy)
lst2 = lst1.copy()    # или lst1.sort(key=reverse)
lst2.reverse()
print(lst2)
print(lst2[:5])
