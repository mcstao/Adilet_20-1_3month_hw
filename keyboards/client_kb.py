from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = KeyboardButton("/start")
quiz = KeyboardButton("/quiz")
location_button = KeyboardButton("Share location", request_location=True)
info_button = KeyboardButton("Share info", request_contact=True)

start_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
start_markup.row(start, quiz)
start_markup.add(location_button, info_button)

cancel_button = KeyboardButton("CANCEL")
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True

).add(cancel_button)

gender_g = KeyboardButton("Я девушка")
gender_b = KeyboardButton("Я парень")
gender_u = KeyboardButton("Я незнаю")
gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True)
gender_markup.row(gender_g, gender_b, gender_u)