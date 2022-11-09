from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

one = KeyboardButton("1️⃣")
two = KeyboardButton("2️⃣")
three = KeyboardButton("3️⃣")
four = KeyboardButton("4️⃣")

keyboard_wheel = ReplyKeyboardMarkup(resize_keyboard=True).add(one).add(two).add(three).add(four)
