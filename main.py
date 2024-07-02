import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand

from config import TOKEN
from handlers.user import user_router

MENU_COMMANDS = [
    BotCommand(command='start', description='Начать игру!'),
    BotCommand(command='level', description='Выбери уровень игры')
]

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(user_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=MENU_COMMANDS, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
