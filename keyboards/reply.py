from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

import util as util

two_colors = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🟥'),
            KeyboardButton(text='⬛️')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите цвет'
)

suits = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=black) for black in util.BLACK_SUITS],
        [KeyboardButton(text=red) for red in util.RED_SUITS],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите масть'
)

cards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'{card}{suit}')
         for card in util.CARDS] for suit in util.SUITS
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите карту'
)

delete = ReplyKeyboardRemove()
