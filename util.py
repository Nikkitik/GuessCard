from random import choice

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'T']
RED_SUITS = ['♦️', '♥️']
BLACK_SUITS = ['♣️', '♠️']
SUITS = RED_SUITS + BLACK_SUITS


def generate_card():
    random_card = choice(CARDS)
    random_suit = choice(SUITS)

    return random_card, random_suit


def correct_answer_print(card, suit):
    return f'Верно! Бот загадал {card}{suit}'


def wrong_answer_print(card, suit):
    return f'Неверно! Бот загадал {card}{suit}'
