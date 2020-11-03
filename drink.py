from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

drinks = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text='Coke'),
        KeyboardButton(text='Black tea')
    ], [
        KeyboardButton(text='Apple juice'),
        KeyboardButton(text='Green tea')
    ]],
    resize_keyboard=True,
    one_time_keyboard=True
)
