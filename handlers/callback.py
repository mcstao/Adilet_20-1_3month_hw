from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


#@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call : types.CallbackQuery):
    markup =InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС",callback_data="button_call_2")
    markup.add(button_call_2)
    question ="Какого цвета была таблетка, которую принимает Нео в фильме “Матрица”?"
    answers = [
        "Красная",
        "Белая",
        "Синяя",
        "Черная"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        open_period=30,
        explanation="очевидно",
        reply_markup=markup

    )

#@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call : types.CallbackQuery):
    markup =InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС",callback_data="button_call_3")
    markup.add(button_call_3)
    question ="Какой национальный вид спорта Канады?"
    answers = [
        "Футбол",
        "Баскетбол",
        "Хоккей",
        "Лакросс"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=3,
        open_period=30,
        explanation="очевидно",
        reply_markup=markup

    )

#@dp.callback_query_handler(lambda call: call.data == "button_call_3")
async def quiz_4(call : types.CallbackQuery):
    markup =InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС",callback_data="button_call_4")
    markup.add(button_call_4)
    question ="В какой стране были проведены первые Олимпийские игры?"
    answers = [
        "Англия",
        "Испания",
        "Греция",
        "Италия"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=30,
        explanation="очевидно",
        reply_markup=markup

    )

#@dp.callback_query_handler(lambda call: call.data == "button_call_4")
async def quiz_5(call : types.CallbackQuery):
    markup =InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС",callback_data="button_call_5")
    markup.add(button_call_5)
    question ="Каково было первоначальное название Нью-Йорка?"
    answers = [
        "Йорк",
        "Новый Амстердам",
        "Готэм",
        "Олд-Йорк"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        open_period=30,
        explanation="очевидно",
        reply_markup=markup

    )

#@dp.callback_query_handler(lambda call: call.data == "button_call_5")
async def quiz_6(call : types.CallbackQuery):
    markup =InlineKeyboardMarkup()
    button_call_6 = InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС",callback_data="button_call_6")
    markup.add(button_call_6)
    question ="Какая страна является самой маленькой в мире?"
    answers = [
        "Мальта",
        "Мальдивы",
        "Ватикан",
        "Монако"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=30,
        explanation="очевидно",
        reply_markup=markup

    )

#@dp.callback_query_handler(lambda call: call.data == "button_call_6")
async def quiz_7(call : types.CallbackQuery):
    markup =InlineKeyboardMarkup()
    button_call_7 = InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС",callback_data="button_call_7")
    markup.add(button_call_7)
    question ="Символом какой сети быстрого питания является клоун?"
    answers = [
        "Макдональдс",
        "Бургер Кинг",
        "KFC",
        "Чиккен"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        open_period=30,
        explanation="очевидно",
        reply_markup=markup

    )

#@dp.callback_query_handler(lambda call: call.data == "button_call_7")
async def quiz_8(call : types.CallbackQuery):
    markup =InlineKeyboardMarkup()
    button_call_8 = InlineKeyboardButton("СЛЕДУЮЩИЙ ВОПРОС",callback_data="button_call_8")
    markup.add(button_call_8)
    question ="Какой город является столицей Австралии?"
    answers = [
        "Мельнбрун",
        "Сидней",
        "Канберра",
        "Аделаида"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=30,
        explanation="очевидно",
        reply_markup=markup

    )

#@dp.callback_query_handler(lambda call: call.data == "button_call_8")
async def quiz_9(call : types.CallbackQuery):

    question ="Какая страна является самой подверженной землетрясениям страной в мире?"
    answers = [
        "Малайзия",
        "Корея",
        "Япония",
        "Китай"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=30,
        explanation="очевидно",


    )


def register_handlers_callback(dp:Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                              lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,
                              lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4,
                              lambda call: call.data == "button_call_3")
    dp.register_callback_query_handler(quiz_5,
                              lambda call: call.data == "button_call_4")
    dp.register_callback_query_handler(quiz_6,
                              lambda call: call.data == "button_call_5")
    dp.register_callback_query_handler(quiz_7,
                              lambda call: call.data == "button_call_6")
    dp.register_callback_query_handler(quiz_8,
                              lambda call: call.data == "button_call_7")
    dp.register_callback_query_handler(quiz_9,
                              lambda call: call.data == "button_call_8")
