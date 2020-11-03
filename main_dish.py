from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_dishes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Hamburger'),
            KeyboardButton(text='Kebab')
        ], [
            KeyboardButton(text='Shawrma'),
            KeyboardButton(text='Sushi')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
