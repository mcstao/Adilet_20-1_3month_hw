from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot,dp
from keyboards.client_kb import start_markup
import random





#@dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС",callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Какой безалкогольный напиток первым был взят в космос?"
    answers = [
        "PEPSI",
        "COLA",
        "FANTA",
        "SPRITE"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        open_period=30,
        explanation="очевидно",
        reply_markup=markup

    )

#@dp.message_handler(commands=["mem"])
async def mem(message:types.Message):

    photos = ["media/1.jpg","media/2.jpg" , "media/3.jpg" ,"media/4.jpg" , "media/5.jpg","media/6.jpg","media/7.jpg"]
    photo = open(random.choice(photos),"rb")
    await bot.send_photo(message.chat.id,photo=photo)


#@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Приветствую {message.from_user.full_name}",
                           reply_markup=start_markup)

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply("Надо ответить на сообщение")

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(start ,commands=["start"])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_message_handler(mem, commands=["mem"])
    dp.register_message_handler(pin,commands=["pin"],commands_prefix="!")