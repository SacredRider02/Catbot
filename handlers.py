import logging
from main import bot, dp
from aiogram.types import Message, CallbackQuery
from config import admin_id
from drink import drinks
from main_dish import main_dishes
from game_choise_keyboard import games, lumberjack_keboard, corsairs_keyboard


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Bot is started')


@dp.message_handler()
async def greeting(message: Message):
    x = message.text
    if x.lower() == 'hello':
        await bot.send_message(chat_id=message.from_user.id,
                               text='Hello there, text me '
                                    '/help to see what can I do')
    elif x == '/help':
        await bot.send_message(chat_id=message.from_user.id,
                               text='Here are my functions: '
                                    '\n/menu to order food;'
                                    '\n/bots to see a '
                                    'list of different chat bots'
                                    '\n/game to choose and play a game'
                                    '/game to choose and play a game')
    elif x == '/menu':
        await message.answer("Choose a food from menu",
                             reply_markup=main_dishes)
    elif x == 'Hamburger' or x == 'Kebab' or x == 'Shawrma' or x == 'Sushi':
        await message.answer(f"You choise {message.text}")
        await message.answer('Now choose a drink', reply_markup=drinks)
    elif x == 'Coke' or x == 'Black tea':
        await message.answer(f'You choise {message.text}')
    elif x == 'Apple juice' or x == 'Green tea':
        await message.answer(f'You choise {message.text}')
    elif message.text == '/bots':
        await message.answer('Here are some fancy bots for groups:\n'
                             '@shmalala\n'
                             '@gamebot\n'
                             '@hangbot'
                             )
        await message.answer('And these are for users:\n'
                             '@spotybot\n'
                             '@gif\n'
                             )
    elif message.text == '/game':
        await message.answer('Choose the game you want to play',
                             reply_markup=games)
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Hello there, '
                                    'text me /help to '
                                    'see what can I do')


@dp.callback_query_handler(text='lumberjack')
async def gaming_one(call: CallbackQuery):
    await call.answer(60)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer(text='You choise Lumberjack!',
                              reply_markup=lumberjack_keboard)


@dp.callback_query_handler(text='corsairs')
async def gaming_two(call: CallbackQuery):
    await call.answer(60)
    callback_data = call.data
    logging.info(f'call={callback_data}')

    await call.message.answer(text='You choise Corsairs!',
                              reply_markup=corsairs_keyboard)
