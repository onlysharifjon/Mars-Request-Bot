from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from keyboards.inline.btn import ruxsat, filiallar
from states.states import *
from loader import dp
from handlers.admin import admin_check

data = {}

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum, {message.from_user.full_name}!", reply_markup=ruxsat)

@dp.callback_query_handler()
async def ruxsat_olish(call: types.CallbackQuery):
    await call.message.delete()
    user_id = int(call.from_user.id)
    if user_id not in data:
        data[user_id] = {}
    data[user_id]['teacher_user_id'] = user_id
    await call.message.answer("""Ism va familyangizni kiriting ⬇️

✅ <i>Bekbayev Sirojiddin</i>
❌ <i>Siroj</i>""")
    await Bolimlar.ism.set()

@dp.message_handler(content_types=types.ContentType.TEXT, state=Bolimlar.ism)
async def get_name(message: types.Message, state: FSMContext):
    user_id = int(message.from_user.id)
    data[user_id]['teacher_name'] = message.text
    await message.answer("""Javob so’rash sanasini to’liq kiriting ⬇️

✅ <i>01.02.2024</i>
❌ <i>1 fev</i>""")
    await Bolimlar.vaqt.set()

@dp.message_handler(content_types=types.ContentType.TEXT, state=Bolimlar.vaqt)
async def get_filial(message: types.Message, state: FSMContext):
    user_id = int(message.from_user.id)
    data[user_id]['teacher_time'] = message.text
    await message.answer("<b>Filialdan birini tanlang</b>", reply_markup=filiallar)
    await Bolimlar.filial.set()

@dp.callback_query_handler(state=Bolimlar.filial)
async def get_group(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    user_id = int(call.from_user.id)
    data[user_id]['filial'] = call.data.upper()
    await call.message.answer(f'Tanlangan filial: <b>{data[user_id]["filial"]}</b>')
    await call.message.answer("""Guruhingizni kiriting ⬇️

✅ BG-1375
❌ bg1375""")
    await Bolimlar.guruh.set()

@dp.message_handler(content_types=types.ContentType.TEXT, state=Bolimlar.guruh)
async def get_orniga(message: types.Message, state: FSMContext):
    user_id = int(message.from_user.id)
    data[user_id]['teacher_group'] = message.text
    await message.answer("""O’rningizga tayinlangan hodim ism va familyasini to’liq kiriting ⬇️

✅ <i>Bekbayev Sirojiddin</i>
❌ <i>Siroj</i>""")
    await Bolimlar.orniga_hodim.set()

@dp.message_handler(content_types=types.ContentType.TEXT, state=Bolimlar.orniga_hodim)
async def get_sabab(message: types.Message, state: FSMContext):
    user_id = int(message.from_user.id)
    data[user_id]['change_teacher'] = message.text
    await message.answer("Javob so’rash sababini to’liq kiriting ⬇️")
    await Bolimlar.sabab.set()

@dp.message_handler(content_types=types.ContentType.TEXT, state=Bolimlar.sabab)
async def yuborildi(message: types.Message, state: FSMContext):
    user_id = int(message.from_user.id)
    data[user_id]["sababi"] = message.text
    await admin_check.save_data(
        data[user_id]['teacher_user_id'],
        data[user_id]['teacher_name'],
        data[user_id]['teacher_time'],
        data[user_id]['filial'],
        data[user_id]['teacher_group'],
        data[user_id]['change_teacher'],
        data[user_id]["sababi"]
    )
    await message.answer("Ma'lumotlar saqlandi. Rahmat!")
    await state.finish()
    print(data)