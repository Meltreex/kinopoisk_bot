from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


def main_bar():
    main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton('Выбор жанра')
    btn2 = KeyboardButton('🅰️ниме')
    btn3 = KeyboardButton('Сериал🎞')
    btn4 = KeyboardButton('Произвольное кино🎥')
    main.add(btn1, btn2, btn3, btn4)
    return main

def genres():
    main = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('Драма😭')
    btn2 = KeyboardButton('Комедия🤣')
    btn3 = KeyboardButton('Триллер🫣')
    btn4 = KeyboardButton('Боевик🤯')
    btn5 = KeyboardButton('Ужасы☠️')
    btn6 = KeyboardButton('Назад⬅️')
    main.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return main



