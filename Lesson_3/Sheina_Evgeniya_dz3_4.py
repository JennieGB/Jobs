import random
n = int(input('Введите количество шуток: '))

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
for word in range(n):
    print(random.choice(nouns), random.choice(adverbs), random.choice(adjectives))
