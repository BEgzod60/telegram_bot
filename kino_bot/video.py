from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
import asyncio
from aiogram.enums.content_type import ContentType



router = Router()

@router.message(F.content_type == ContentType.VIDEO)
async def send_video(message: types.Message):
    video_id = message.video.file_id
    
    with open("links.txt", "a") as link:
        link.write(f"  {video_id}\n")