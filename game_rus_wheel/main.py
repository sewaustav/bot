from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command, Text
from aiogram import Bot, Dispatcher, executor, types
import logging
from config import *
from keyboard import *
from random import randint

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def game(current, r):
    if r <= current:
        ret = "вы проиграли"
        return ret
    if r > current:
        ret = "Повезло, выстрел оказался холостым"
        return ret

dp.message_handler(commands=["start"])
async def stsrt(message: types.Message):
    await message.answer("/rul")

dp.message_handler(commands=["rul"])
async def rul(message: types.Message):
    await message.answer("введите количество патронов", reply_markup=keyboard_wheel)

dp.message_handler(Text(equals=["1️⃣"]))
async def one_f(message: types.Message):
    a = randint(1, 8)
    aa = game(1, a)
    await message.answer(aa)

dp.message_handler(Text(equals=["2️⃣"]))
async def two_f(message: types.Message):
    b = randint(1, 8)
    bb = game(2, b)
    await message.answer(bb)

dp.message_handler(Text(equals=["3️⃣"]))
async def three_f(message: types.Message):
    c = randint(1, 8)
    cc = game(3, c)
    await message.answer(cc)

dp.message_handler(Text(equals=["4️⃣"]))
async def four_f(message: types.Message):
    d = randint(1, 8)
    dd = game(4, d)
    await message.answer(dd)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)