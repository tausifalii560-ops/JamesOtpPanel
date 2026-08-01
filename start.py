from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.user import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    text = f"""
✨ <b>Welcome {message.from_user.first_name}</b>

💰 Balance : $0.00
📦 Orders : 0

Choose an option below.
"""

    await message.answer(
        text,
        reply_markup=main_menu(message.from_user.id),
    )
