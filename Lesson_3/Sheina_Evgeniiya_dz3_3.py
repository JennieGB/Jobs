def thesaurus(*names):
    dict_names = dict()
    for n in names:
        dict_names.setdefault(n[0], [])
        dict_names[n[0]].append(n)
    return dict_names
print(thesaurus("Иван", "Мария", "Петр", "Илья"))
