from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

bot = Bot(
    token="8345524927:AAHas0HPcbEwph-gR_iS7py2iBEU5B5Mcg0",
    default= DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()