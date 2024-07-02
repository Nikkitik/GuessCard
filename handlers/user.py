from random import choice

from aiogram import F, Router

from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import keyboards.inline as inline_keyboard
import keyboards.reply as reply_keyboard

user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Здравствуй мой друг!\nВыбери уровень игры и начнем',
                         reply_markup=inline_keyboard.level)


@user_router.message(Command('level'))
async def level(message: Message):
    await message.edit_text('Выбери уровень игры и начнем',
                            reply_markup=inline_keyboard.level)


@user_router.message((F.text == '🟥') | (F.text == '⬛️'))
async def compare_answers(message: Message):
    card, suit = generate_card()

    answer = message.text

    correct_answer_print = f'Верно! Бот загадал {card}{suit}'
    wrong_answer_print = f'Неверно! Бот загадал {card}{suit}'

    if answer == '🟥' and suit in ['♦️', '♥️']:
        await message.answer(correct_answer_print)
    elif answer == '⬛️' and suit in ['♣️', '♠️']:
        await message.answer(correct_answer_print)
    else:
        await message.answer(wrong_answer_print)


@user_router.message(F.text.in_({'♦️', '♥️', '♣️', '♠️'}))
async def compare_answers(message: Message):
    card, suit = generate_card()

    answer = message.text

    correct_answer_print = f'Верно! Бот загадал {card}{suit}'
    wrong_answer_print = f'Неверно! Бот загадал {card}{suit}'

    if answer == suit:
        await message.answer(correct_answer_print)
    else:
        await message.answer(wrong_answer_print)


def generate_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'T']
    suits = ['♦️', '♥️', '♣️', '♠️']

    random_card = choice(cards)
    random_suit = choice(suits)

    return random_card, random_suit


@user_router.callback_query(F.data == 'level_color')
async def level_color(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В этой игре необходимо отгадать цвет масти',
                                  reply_markup=reply_keyboard.two_colors)


@user_router.callback_query(F.data == 'level_suit')
async def level_suit(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В этой игре необходимо отгадать масть',
                                  reply_markup=reply_keyboard.suits)


@user_router.callback_query(F.data == 'level_card')
async def level_card(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В этой игре необходимо отгадать масть',
                                  reply_markup=reply_keyboard.cards)
