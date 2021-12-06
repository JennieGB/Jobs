import random
joke = []
nouns = random.choice(["автомобиль", "лес", "огонь", "город", "дом"])
adverbs = random.choice(["сегодня", "вчера", "завтра", "позавчера", "ночью"])
adjectives = random.choice(["веселый", "яркий", "зеленый", "утопичный", "мягкий"])
for word in nouns, adverbs, adjectives:
    joke.append(f'{nouns} {adverbs} {adjectives}')
print(joke)
