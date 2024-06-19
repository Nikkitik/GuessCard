from random import choice
import telebot

from keys import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()

    red_button = telebot.types.KeyboardButton('🟥')
    black_button = telebot.types.KeyboardButton('⬛️')

    keyboard.row(red_button)
    keyboard.row(black_button)

    bot.send_message(message.chat.id, 'Здравствуй мой друг!\nВ этой игре тебе необходимо определить цвет масти!',
                     reply_markup=keyboard)

    bot.register_next_step_handler(message, compare_answers)


def compare_answers(message):
    card, suit = generate_card()

    answer = message.text

    correct_answer_print = f'Верно! Бот загадал {card}{suit}'
    wrong_answer_print = f'Неверно! Бот загадал {card}{suit}'

    if answer == '🟥' and suit in ['♦️', '♥️']:
        bot.send_message(message.chat.id, correct_answer_print)
    elif answer == '⬛️' and suit in ['♣️', '♠️']:
        bot.send_message(message.chat.id, correct_answer_print)
    else:
        bot.send_message(message.chat.id, wrong_answer_print)

    start(message)


def generate_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'T']
    suits = ['♦️', '♥️', '♣️', '♠️']

    random_card = choice(cards)
    random_suit = choice(suits)

    return random_card, random_suit


bot.polling(non_stop=True)
