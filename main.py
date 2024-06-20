import asyncio
from random import choice
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import BotCommand

from keys import TOKEN
from keyboards import reply

MENU_COMMANDS = [
    BotCommand(command='start', description='Начать игру!')
]

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Здравствуй мой друг!\nВ этой игре тебе необходимо определить цвет масти!',
                         reply_markup=reply.two_color_keyboard)


@dp.message((F.text == '🟥') | (F.text == '⬛️'))
async def compare_answers(message: types.Message):
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

    start(message)


def generate_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'T']
    suits = ['♦️', '♥️', '♣️', '♠️']

    random_card = choice(cards)
    random_suit = choice(suits)

    return random_card, random_suit


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=MENU_COMMANDS, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

asyncio.run(main())
