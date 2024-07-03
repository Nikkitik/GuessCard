from aiogram import F, Router

from aiogram.types import Message

import util as util

filters_router = Router()


@filters_router.message((F.text == '🟥') | (F.text == '⬛️'))
async def compare_answers(message: Message):
    card, suit = util.generate_card()

    answer = message.text

    if answer == '🟥' and suit in util.RED_SUITS:
        await message.answer(util.correct_answer_print(card, suit))
    elif answer == '⬛️' and suit in util.BLACK_SUITS:
        await message.answer(util.correct_answer_print(card, suit))
    else:
        await message.answer(util.wrong_answer_print(card, suit))


@filters_router.message(F.text.in_(util.SUITS))
async def compare_answers(message: Message):
    card, suit = util.generate_card()

    answer = message.text

    if answer == suit:
        await message.answer(util.correct_answer_print(card, suit))
    else:
        await message.answer(util.wrong_answer_print(card, suit))
