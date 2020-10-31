from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import lumberjack_URL, corsairs_URL

games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Lumberjack', callback_data='lumberjack'),
            InlineKeyboardButton(text='Corsairs', callback_data='corsairs')
        ]
    ]
)

lumberjack_keboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Play here', url=lumberjack_URL)
        ]
    ]
)

corsairs_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Play here', url=corsairs_URL)
        ]
    ]
)