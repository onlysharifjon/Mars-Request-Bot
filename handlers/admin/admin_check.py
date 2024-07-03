from aiogram import types
from keyboards.inline.btn import button, button_for_admin, ruxsat
from loader import bot, dp
from handlers.users import start


async def save_data(teacher_user_id, teacher_name, teacher_time, filial, teacher_group, change_teacher, sababi):
    global current_user_id, current_teacher_name, current_teacher_time, current_filial, current_teacher_group, current_change_teacher, current_sababi

    current_user_id = teacher_user_id
    current_teacher_name = teacher_name
    current_teacher_time = teacher_time
    current_filial = filial
    current_teacher_group = teacher_group
    current_change_teacher = change_teacher
    current_sababi = sababi


    await bot.send_message(
            chat_id=current_user_id,
            text=f'''
🧍‍♂️Hodim : <b>{current_teacher_name}</b>
🗓 Sana : <b>{current_teacher_time}</b>
🏢 Filial : <b>{current_filial}</b>
🗂️ Guruh : <b>{current_teacher_group}</b>
🧍‍♂️ O'rniga tayinlanadigan hodim : <b>{current_change_teacher}</b>
📝 Sabab : <b>{current_sababi}</b>
            ''',

            reply_markup=button,
        )

user_messages = {}


@dp.callback_query_handler(text='tasdiqlash')
async def process_confirm(callback_query: types.CallbackQuery):
    admin_chat_id = 5120362988

    admin_message = await bot.send_message(
        chat_id=admin_chat_id,
        text=f'''
    🧍‍♂️Hodim : <b>{current_teacher_name}</b>
    🗓 Sana : <b>{current_teacher_time}</b>
    🏢 Filial : <b>{current_filial}</b>
    🗂️ Guruh : <b>{current_teacher_group}</b>
    🧍‍♂️ O'rniga tayinlanadigan hodim : <b>{current_change_teacher}</b>
    📝 Sabab : <b>{current_sababi}</b>
            ''',
        reply_markup=button_for_admin,
        parse_mode="HTML"
    )

    user_message = await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f"""So’rovingiz qabul qilindi.Javobini kuting.\nSizning ma’lumotlaringiz ⬇️\n
🧍‍♂️Hodim : <b>{current_teacher_name}</b>
🗓 Sana : <b>{current_teacher_time}</b>
🏢 Filial : <b>{current_filial}</b>
🗂️ Guruh : <b>{current_teacher_group}</b>
🧍‍♂️ O'rniga tayinlanadigan hodim : <b>{current_change_teacher}</b>
📝 Sabab : <b>{current_sababi}</b>
""",
        parse_mode="HTML"
    )

    user_messages[callback_query.from_user.id] = {
        "admin_message_id": admin_message.message_id,
        "user_message_id": user_message.message_id
    }

    await callback_query.message.delete()


@dp.callback_query_handler(text='admin_uchun_tasdiqlash')
async def process_admin_confirm(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Siz ma'lumotlarni tasdiqladingiz.")

    if int(current_user_id) in user_messages:
        messages = user_messages[current_user_id]
        await bot.delete_message(chat_id=current_user_id, message_id=messages["user_message_id"])
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=messages["admin_message_id"])

    await bot.send_message(
        int(current_user_id),
        f"""Sizning so'rovingiz <b>TASDIQLANDI✅</b>.\n
🧍‍♂️Hodim : <b>{current_teacher_name}</b>
🗓 Sana : <b>{current_teacher_time}</b>
🏢 Filial : <b>{current_filial}</b>
🗂️ Guruh : <b>{current_teacher_group}</b>
🧍‍♂️ O'rniga tayinlanadigan hodim : <b>{current_change_teacher}</b>
📝 Sabab : <b>{current_sababi}</b>
""",
        reply_markup=ruxsat,
        parse_mode="HTML"
    )

    group_chat_id = -4270625456
    await bot.send_message(
        chat_id=group_chat_id,
        text=f'''
<b>✅TASDIQLANDI</b>

🧍‍♂️Hodim : <b>{current_teacher_name}</b>
🗓 Sana : <b>{current_teacher_time}</b>
🏢 Filial : <b>{current_filial}</b>
🗂️ Guruh : <b>{current_teacher_group}</b>
🧍‍♂️ O'rniga tayinlanadigan hodim : <b>{current_change_teacher}</b>
📝 Sabab : <b>{current_sababi}</b>
''',
        parse_mode="HTML"
    )


@dp.callback_query_handler(text='rad_etish')
async def process_reject(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Sizning ma'lumotlaringiz o'chirildi.", reply_markup=ruxsat)

    await callback_query.message.delete()


@dp.callback_query_handler(text='admin_rad_etish')
async def process_reject(callback_query: types.CallbackQuery):
    if int(current_user_id) in user_messages:
        messages = user_messages[current_user_id]
        await bot.delete_message(chat_id=current_user_id, message_id=messages["user_message_id"])
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=messages["admin_message_id"])
    await bot.send_message(callback_query.from_user.id, "Siz ma'lumotlarni rad etdingiz.")
    await bot.send_message(current_user_id, f"""Sizning ma'lumotlaringiz <b>RAD ETILDI❌</b>. \n 
🧍‍♂️Hodim : <b>{current_teacher_name}</b>
🗓 Sana : <b>{current_teacher_time}</b>
🏢 Filial : <b>{current_filial}</b>
🗂️ Guruh : <b>{current_teacher_group}</b>
🧍‍♂️ O'rniga tayinlanadigan hodim : <b>{current_change_teacher}</b>
📝 Sabab : <b>{current_sababi}</b>""", reply_markup=ruxsat)

    group_chat_id = -4270625456
    await bot.send_message(
        chat_id=group_chat_id,
        text=f'''
<b>Rad etildi ❌ </b>

🧍‍♂️Hodim : <b>{current_teacher_name}</b>
🗓 Sana : <b>{current_teacher_time}</b>
🏢 Filial : <b>{current_filial}</b>
🗂️ Guruh : <b>{current_teacher_group}</b>
🧍‍♂️ O'rniga tayinlanadigan hodim : <b>{current_change_teacher}</b>
📝 Sabab : <b>{current_sababi}</b>


        ''',

    )
