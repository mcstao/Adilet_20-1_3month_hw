
from aiogram import types, Dispatcher
from config import bot
from config import ADMIN
import random


async def kick(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMIN:
            await message.reply("У вас нет  права на это")
        elif not message.reply_to_message:
            await message.reply("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
            await message.answer(f"{message.from_user.first_name} братан "
                                 f"кикнул участника {message.reply_to_message.from_user.full_name}")
    else:
        await message.reply("Пиши в группе!")






def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(kick, commands=['kick'], commands_prefix="!/")
