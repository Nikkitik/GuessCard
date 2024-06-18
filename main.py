from random import choice

print('Здравствуй мой друг.\nВ этой игре тебе необходимо определить цвет масти!')
print()

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'T']
suits = ['♦️', '♥️', '♣️', '♠️']

random_card = choice(cards)
random_suit = choice(suits)

answer = input('Какой цвет масти загадал бот?\nВведите К(Красная) или Ч(Черная)\n')

correct_answer = f'Верно! Бот загадал {random_card}{random_suit}'
wrong_answer = f'Неверно! Бот загадал {random_card}{random_suit}'

print()

if answer.upper == 'К' and random_suit in ['♦️', '♥️']:
    print(correct_answer)
elif answer.upper == 'Ч' and random_suit in ['♣️', '♠️']:
    print(correct_answer)
else:
    print(wrong_answer)
