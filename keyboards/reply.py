from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

two_color_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🟥'),
            KeyboardButton(text='⬛️')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите цвет'
)

delete_keyboard = ReplyKeyboardRemove()
