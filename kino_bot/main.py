from aiogram import  types, Router
from aiogram.filters import Command, CommandStart
import asyncio
from aiogram.fsm.context import FSMContext 
from loaderr import bot, dp
from aiogram.client.default import DefaultBotProperties
from video import router as video_r


router = Router()

@router.message(CommandStart())
async def start_bot(message: types.Message):
    fullname = message.from_user.full_name

    await message.reply(
        text= f"""
Asslamu alaykum <i>{fullname}</i>
Botimizga hush kelibsiz bu bot jahondagi eng zo'r filmlarni oz ichiga olgan❗️
<b>Kino kodini kiritishingiz mumkin</b>
"""
    )


@router.message(Command('help'))
async def help(message:types.Message):
    
    text = """Help buyruqlari:

/start - <b>Botni ishga tushirish</b>
/help - <b>Yordam</b>
Bu bot sizga jahon miqyosidagi eng zo'r kinolarni topishda yordam beradi!
"""

    await message.reply(
        text=text
    )

@router.message(Command('admin')) # admin komandasi bosilganda uni ushlab oladi 
async def admin_bot(message: types.Message):
    await message.answer(
        text = f"@begzodmavlonov"
    )


async def main():
    print("Bot ishga tushdi...")
    try:
        await bot.send_message(
            chat_id=6127579611,
            text="Bot ishga tushdi"
        )
    except:
        pass
    dp.include_router(router)
    dp.include_router(video_r)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())