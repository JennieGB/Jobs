number = input('Введите число от 0 до 10 на английском: ')
dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}
def num_translate(english):
    if english[0] == english[0].upper():
        english = english.lower()
        return dictionary[english].capitalize()
    else:
        return dictionary.get(english)
print(num_translate(number))
