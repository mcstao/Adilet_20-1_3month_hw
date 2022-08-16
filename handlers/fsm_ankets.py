from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State,StatesGroup


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    age = State()
    gender = State()
    region = State()

async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.photo.set()
        await message.answer(f"Привет {message.from_user.full_name}"
                             f"скинь фотку")
    else:
        await message.reply("Пиши в личку!")

async def load_photo(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data["id"]= message.from_user.id
        data["username"] = f"@{message.from_user.username}"
        data["photo"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Как тебя зовут?")

async def load_name(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMAdmin.next()
    await message.answer("Какого года рождения?")

async def load_age(message: types.Message, state:FSMContext):
    try:
        if  int(message.text) < 2008 and int(message.text) < 1950:
            await message.answer("Доступ запрещен!!")
        else:
            async with state.proxy() as data:
                data["age"] = int(message.text)
            await FSMAdmin.next()
            await message.answer("Какого пола?")
    except:
        await message.answer("Пиши числами")

def register_handlers_fsmanketa(dp:Dispatcher):
    dp.register_message_handler(fsm_start,commands=["reg"])
    dp.register_message_handler(load_photo,state=FSMAdmin.photo,
                                content_types=["photo"])
    dp.register_message_handler(load_name,state=FSMAdmin.name)
    dp.register_message_handler(load_age,state=FSMAdmin)