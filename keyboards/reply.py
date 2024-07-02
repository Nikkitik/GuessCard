from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

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
        [
            KeyboardButton(text='♠️'),
            KeyboardButton(text='♣️')
        ],
        [
            KeyboardButton(text='♦️'),
            KeyboardButton(text='♥️')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите масть'
)

cards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='2♠️'),
            KeyboardButton(text='3♠️'),
            KeyboardButton(text='4♠️'),
            KeyboardButton(text='5♠️'),
            KeyboardButton(text='6♠️'),
            KeyboardButton(text='7♠️'),
            KeyboardButton(text='8♠️'),
            KeyboardButton(text='9♠️'),
            KeyboardButton(text='10♠️'),
            KeyboardButton(text='J♠️'),
            KeyboardButton(text='Q♠️'),
            KeyboardButton(text='K♠️'),
            KeyboardButton(text='T♠️')
        ],
        [
            KeyboardButton(text='2♣️'),
            KeyboardButton(text='3♣️'),
            KeyboardButton(text='4♣️'),
            KeyboardButton(text='5♣️'),
            KeyboardButton(text='6♣️'),
            KeyboardButton(text='7♣️'),
            KeyboardButton(text='8♣️'),
            KeyboardButton(text='9♣️'),
            KeyboardButton(text='10♣️'),
            KeyboardButton(text='J♣️'),
            KeyboardButton(text='Q♣️'),
            KeyboardButton(text='K♣️'),
            KeyboardButton(text='T♣️'),
        ],
        [
            KeyboardButton(text='2♦️'),
            KeyboardButton(text='3♦️'),
            KeyboardButton(text='4♦️'),
            KeyboardButton(text='5♦️'),
            KeyboardButton(text='6♦️'),
            KeyboardButton(text='7♦️'),
            KeyboardButton(text='8♦️'),
            KeyboardButton(text='9♦️'),
            KeyboardButton(text='10♦️'),
            KeyboardButton(text='J♦️'),
            KeyboardButton(text='Q♦️'),
            KeyboardButton(text='K♦️'),
            KeyboardButton(text='T♦️'),
        ],
        [
            KeyboardButton(text='2♥️'),
            KeyboardButton(text='3♥️'),
            KeyboardButton(text='4♥️'),
            KeyboardButton(text='5♥️'),
            KeyboardButton(text='6♥️'),
            KeyboardButton(text='7♥️'),
            KeyboardButton(text='8♥️'),
            KeyboardButton(text='9♥️'),
            KeyboardButton(text='10♥️'),
            KeyboardButton(text='J♥️'),
            KeyboardButton(text='Q♥️'),
            KeyboardButton(text='K♥️'),
            KeyboardButton(text='T♥️'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите карту'
)

delete = ReplyKeyboardRemove()
