from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

level = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Угадай цвет масти',
                              callback_data='level_color')],
        [InlineKeyboardButton(text='Угадай масть',
                              callback_data='level_suit')],
        [InlineKeyboardButton(text='Угадай карту',
                              callback_data='level_card')],
    ]
)
