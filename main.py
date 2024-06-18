from random import choice

print('Здравствуй мой друг.\nВ этой игре тебе необходимо определить цвет масти!')
print()

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'T']
suits = ['♦️', '♥️', '♣️', '♠️']

correct_answers = ['Красная', 'К', 'к', 'Черная', 'Ч', 'ч']

random_card = choice(cards)
random_suit = choice(suits)

answer = input(
    'Какой цвет масти загадал бот?\nВведите К(Красная) или Ч(Черная)\n')

correct_answer_print = f'Верно! Бот загадал {random_card}{random_suit}'
wrong_answer_print = f'Неверно! Бот загадал {random_card}{random_suit}'

print()

while not answer in correct_answers:
    answer = input(
        'Введите букву К или Ч.\nВы также можете ввести слово целиком Красная или Черная\n')
    print()

if answer.upper == 'К' and random_suit in ['♦️', '♥️']:
    print(correct_answer_print)
elif answer.upper == 'Ч' and random_suit in ['♣️', '♠️']:
    print(correct_answer_print)
else:
    print(wrong_answer_print)
