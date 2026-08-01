from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMINS


def main_menu(user_id: int):
    buttons = [
        [
            InlineKeyboardButton(text="🛒 Buy Products", callback_data="buy"),
            InlineKeyboardButton(text="💳 Deposit", callback_data="deposit"),
        ],
        [
            InlineKeyboardButton(text="📦 My Orders", callback_data="orders"),
            InlineKeyboardButton(text="👤 Profile", callback_data="profile"),
        ],
        [
            InlineKeyboardButton(text="🎁 Referral", callback_data="referral"),
            InlineKeyboardButton(text="💬 Support", callback_data="support"),
        ],
    ]

    if user_id in ADMINS:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="🔐 Admin Panel",
                    callback_data="admin",
                )
            ]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons)
