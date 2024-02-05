import json

import aiogram.utils.exceptions
import requests
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Command, ContentTypeFilter, Text
import logging
import keyboard as kb

with open(r"путь к файлу token_file.json на вашем пк, например: D:\Projects\Film\token_file.json") as file:
    data = json.load(file)

BOT_TOKEN = data['BOT_TOKEN']

TOKEN_KINO = data['TOKEN_KINO']

url = 'https://api.kinopoisk.dev/'

headers = {'accept': 'application/json', 'X-API-KEY': TOKEN_KINO}


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start_func(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Привет! Я помогу тебе выбрать картину для просмотра.',
                           reply_markup=kb.main_bar())

@dp.message_handler(Text(equals='Назад⬅️'))
async def back_func(msg: types.Message):
    await bot.send_message(msg.from_user.id, f'Назад',
                           reply_markup=kb.main_bar())

@dp.message_handler(Text(equals='Выбор жанра'))
async def choose_genre(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Выбери интересующий жанр!', reply_markup=kb.genres())

@dp.message_handler(Text(equals='Произвольное кино🎥'))
async def get_random_movie(msg: types.Message):

    r = requests.get(url + 'v1.4/movie/random', headers=headers)
    if r.status_code == 200:
        title = r.json()['name']
        description = r.json()['description']
        year = r.json()['year']
        poster = r.json()['poster']['url']


        await bot.send_message(msg.from_user.id, f'Название: {title}')
        await bot.send_message(msg.from_user.id, f'Год выхода: {year}')
        await bot.send_photo(msg.from_user.id, photo=poster, caption=description)


@dp.message_handler(Text(equals='Сериал🎞'))
async def get_random_tvseries(msg: types.Message):
    response = requests.get(
        url='https://api.kinopoisk.dev/v1.4/movie/random',
        params={
                "type": ['tv-series', '!anime', '!movie'],
                "year": '1990-2023'
        },
        headers=headers
    )
    movies = response.json()
    await bot.send_message(msg.from_user.id, f'Название: {movies["name"]}')
    await bot.send_message(msg.from_user.id, f'Год выхода: {movies["year"]}')
    await bot.send_photo(msg.from_user.id, photo=movies['poster']['url'], caption=movies["description"])

@dp.message_handler(text='Драма😭')
async def choose_genre_drama(msg: types.Message):
    response = requests.get(
        url='https://api.kinopoisk.dev/v1.4/movie/random',
        params={
            "genres.name": ['драма'],
            "year": '1990-2023'
        },
        headers=headers
    )
    movies = response.json()
    await bot.send_message(msg.from_user.id, f'Название: {movies["name"]}')
    await bot.send_message(msg.from_user.id, f'Год выхода: {movies["year"]}')
    await bot.send_photo(msg.from_user.id, photo=movies['poster']['url'], caption=movies["description"])

@dp.message_handler(Text(equals='Ужасы☠️'))
async def choose_genre_horrors(msg: types.Message):
    response = requests.get(
        url='https://api.kinopoisk.dev/v1.4/movie/random',
        params={
            "genres.name": ['ужасы'],
            "year": '1990-2023'
        },
        headers=headers
    )
    movies = response.json()
    await bot.send_message(msg.from_user.id, f'Название: {movies["name"]}')
    await bot.send_message(msg.from_user.id, f'Год выхода: {movies["year"]}')
    await bot.send_photo(msg.from_user.id, photo=movies['poster']['url'], caption=movies["description"])


@dp.message_handler(Text(equals='Триллер🫣'))
async def choose_genre_thriller(msg: types.Message):
    response = requests.get(
        url='https://api.kinopoisk.dev/v1.4/movie/random',
        params={
            "genres.name": ['триллер'],
            "year": '1990-2023'
        },
        headers=headers
    )
    movies = response.json()
    await bot.send_message(msg.from_user.id, f'Название: {movies["name"]}')
    await bot.send_message(msg.from_user.id, f'Год выхода: {movies["year"]}')
    await bot.send_photo(msg.from_user.id, photo=movies['poster']['url'], caption=movies["description"])

@dp.message_handler(Text(equals='Боевик🤯'))
async def choose_genre_action(msg: types.Message):
    response = requests.get(
        url='https://api.kinopoisk.dev/v1.4/movie/random',
        params={
            "genres.name": ['боевик'],
            "year": '1990-2023'
        },
        headers=headers
    )
    movies = response.json()
    await bot.send_message(msg.from_user.id, f'Название: {movies["name"]}')
    await bot.send_message(msg.from_user.id, f'Год выхода: {movies["year"]}')
    await bot.send_photo(msg.from_user.id, photo=movies['poster']['url'], caption=movies["description"])

@dp.message_handler(Text(equals='Комедия🤣'))
async def choose_genre_comedy(msg: types.Message):
    response = requests.get(
        url='https://api.kinopoisk.dev/v1.4/movie/random',
        params={
            "genres.name": ['комедия'],
            "year": '1990-2023'
        },
        headers=headers
    )
    movies = response.json()
    await bot.send_message(msg.from_user.id, f'Название: {movies["name"]}')
    await bot.send_message(msg.from_user.id, f'Год выхода: {movies["year"]}')
    await bot.send_photo(msg.from_user.id, photo=movies['poster']['url'], caption=movies["description"])


@dp.message_handler(Text(equals='🅰️ниме'))
async def get_random_anime(msg: types.Message):
    response = requests.get(
        url='https://api.kinopoisk.dev/v1.4/movie/random',
        params={
                "type": ['!tv-series', 'anime', '!animated-series', '!cartoon', '!movie'],
                "year": '2018-2023'
        },
        headers=headers
    )

    movies = response.json()
    await bot.send_message(msg.from_user.id, f'Название: {movies["name"]}')
    await bot.send_message(msg.from_user.id, f'Год выхода: {movies["year"]}')
    await bot.send_photo(msg.from_user.id, photo=movies['poster']['url'], caption=movies["description"])


@dp.message_handler()
async def echo_func(msg: types.Message):
    query = msg.text
    params = {'query':  query}
    response = requests.get(
        'https://api.kinopoisk.dev/v1.4/movie/search',
        headers=headers,
        params=params
    )
    if response.status_code == 200:
        movies = response.json()
        await bot.send_message(msg.from_user.id, f'Название: {movies["docs"][0]["name"]}')
        await bot.send_message(msg.from_user.id, f'Год выхода: {movies["docs"][0]["year"]}')
        await bot.send_photo(msg.from_user.id, photo=movies['docs'][0]['poster']['url'], caption=movies['docs'][0]['description'], reply_markup=kb.add_list())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
