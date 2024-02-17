import asyncio, logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile, URLInputFile
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from random import randint
from emoji import emojize
from sys import stdout

from SDK import *

from data_base import *



dp = Dispatcher()

TOKEN = "6787488978:AAEbgz4vFt2nheAzLvLLus49HxUoEzrIx0c"
NAME = "META UKRAINE GTA"

MainMenu = {
    "Big-Buttons": [
        types.InlineKeyboardButton(text = "📕 Інформація", callback_data='info_callback' ),
        types.InlineKeyboardButton(text = "🔒 Прив'язати ігровий акаунт", callback_data = "connect_game_account" ),
        types.InlineKeyboardButton(text = "🔑 Відновити пароль до акаунту", url = "https://meta-gta.com.ua/restore.php" )
    ],
    "Links": [
        types.InlineKeyboardButton(text="🌐 Сайт", url = "https://meta-gta.com.ua/"),
        types.InlineKeyboardButton(text="📖 Форум", url = "https://forum.meta-gta.com.ua/"),
        types.InlineKeyboardButton(text="🏪 Магазин", url = "https://meta-gta.com.ua/donate.php"),
    ]
}




# MTA CONTROLLER
from pprint import pprint

mta = MTA()



