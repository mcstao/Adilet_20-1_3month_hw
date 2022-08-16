from aiogram import types, Dispatcher
from config import bot,to
import random
from config import ADMIN




#@dp.message_handler()
async def echo(message:types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) * int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)
    await bot.forward_message(to, message.chat.id, message.message_id)
    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text) * int(message.text))
    else:
        await bot.send_message(message.chat.id, message.text)
    await bot.forward_message(to, message.chat.id, message.message_id)
    bad_words = ['java', 'bitch', 'lox', 'жинди', 'лошок']
    username = f"@{message.from_user.username}" if message.from_user.username is not None else ""
    for word in bad_words:
        if word in message.text.lower():
            await bot.send_message(
                message.chat.id,
                f"Не матерись {message.from_user.full_name}, "
                f"сам ты {word} {username}"
            )
            await bot.delete_message(message.chat.id, message.message_id)
    good_words_women = ["прекрасна","красива","неземная","соска","богиня"]
    username1 = f"@{message.from_user.username}" if message.from_user.username is not None else ""
    for word in good_words_women:
        if word in message.text.lower():
            await message.answer(

                f"да она такая {message.from_user.full_name}, "
                f"полностью согласен {word} {username1}"
            )
            await bot.pin_chat_message(message.chat.id,message.message_id)


    dices=["⚽️","🏀","🎲","🎯","🎳","🎰"]
    if message.text.startswith("game"):
        if message.chat.type != "private":
            if message.from_user.id not in ADMIN:
                await message.reply("У вас нет права на это")
            else:
                await bot.send_dice(message.chat.id, emoji=random.choice(dices))

        else:
            await message.reply("Пиши в группе!")
    if message.text == 'dice':
        a = await bot.send_dice(message.chat.id, emoji='🎲')
        print(a.dice.value)
        await bot.send_message(message.chat.id,"Первый мой")
        b = await bot.send_dice(message.chat.id,emoji="🎲")
        print(b.dice.value)
        await bot.send_message(message.chat.id,
                               f"Второй {message.from_user.full_name}")
        if a.dice.value > b.dice.value:
            await bot.send_message(message.chat.id,
                                   f"Я победил тебя хе-хе-хе){message.from_user.full_name}")
        elif b.dice.value > a.dice.value:
            await bot.send_message(message.chat.id,
                                   f"{message.from_user.full_name} победил 🙁")
        else:
            await bot.send_message(message.chat.id,
                                   f"{message.from_user.full_name} повезло что ничья")


def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(echo)