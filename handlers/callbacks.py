from aiogram import F, Router

from aiogram.types import CallbackQuery
import keyboards.reply as reply_keyboard

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'level_color')
async def level_color(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В этой игре необходимо отгадать цвет масти',
                                  reply_markup=reply_keyboard.two_colors)


@callbacks_router.callback_query(F.data == 'level_suit')
async def level_suit(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В этой игре необходимо отгадать масть',
                                  reply_markup=reply_keyboard.suits)


@callbacks_router.callback_query(F.data == 'level_card')
async def level_card(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('В этой игре необходимо отгадать масть',
                                  reply_markup=reply_keyboard.cards)
