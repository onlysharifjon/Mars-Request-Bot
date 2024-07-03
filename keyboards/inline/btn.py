from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Yuborish", callback_data="tasdiqlash")],
        [InlineKeyboardButton(text="❌ Qaytadan kiritish", callback_data="rad_etish")]
    ]
)

button_for_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="admin_uchun_tasdiqlash")],
        [InlineKeyboardButton(text="❌ Rad etish", callback_data="admin_rad_etish")]
    ]
)

filiallar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🏢Tinchlik", callback_data="tinchlik")],
        [InlineKeyboardButton(text="🏢Yunusobod", callback_data="yunusobod")],
        [InlineKeyboardButton(text="🏢Chilonzor", callback_data="chilonzor")],
        [InlineKeyboardButton(text="🏢Maksim Gorkiy", callback_data="maksim Gorkiy")],
        [InlineKeyboardButton(text="🏢Sergeli", callback_data="sergeli")]

    ]
)

ruxsat = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ruxsat olish uchun bosing ✅ ", callback_data="ruxsat_olish")]
    ]
)
