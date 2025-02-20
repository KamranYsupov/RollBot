import os

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'), default=DefaultBotProperties())
dp = Dispatcher()