from aiogram import Router

from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import keyboards.inline as inline_keyboard

commands_router = Router()


@commands_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Здравствуй мой друг!\nВыбери уровень игры и начнем',
                         reply_markup=inline_keyboard.level)


@commands_router.message(Command('level'))
async def level(message: Message):
    await message.answer('Выбери уровень игры и начнем',
                         reply_markup=inline_keyboard.level)
