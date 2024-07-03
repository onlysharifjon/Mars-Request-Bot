from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from keyboards.inline.btn import ruxsat, filiallar
from states.states import *
from loader import dp
from database import *



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum, {message.from_user.full_name}!", reply_markup=ruxsat)


@dp.callback_query_handler()
async def ruxsat_olish(call: types.CallbackQuery):
    await call.message.delete()
    global teacher_user_id
    teacher_user_id = call.from_user.id
    await call.message.answer("""Ism va familyangizni kiriting ⬇️

✅ <i>Bekbayev Sirojiddin</i>
❌ <i>Siroj</i>""")
    await Bolimlar.ism.set()


@dp.message_handler(content_types="text", state=Bolimlar.ism)
async def get_name(message: types.Message, state: FSMContext):
    global teacher_name
    teacher_name = message.text
    await state.finish()
    await message.answer("""Javob so’rash sanasini to’liq kiriting ⬇️

✅ <i>01.02.2024</i>
❌ <i>1 fev</i>""")
    await Bolimlar.vaqt.set()


@dp.message_handler(content_types="text", state=Bolimlar.vaqt)
async def get_filial(message: types.Message, state: FSMContext):
    global teacher_time
    teacher_time = message.text
    await state.finish()
    await message.answer("<b>Filialdan birini tanlang</b>", reply_markup=filiallar)
    await Bolimlar.filial.set()


@dp.callback_query_handler(state=Bolimlar.filial)
async def get_group(call: types.CallbackQuery, state: FSMContext):
    global filial
    await call.message.delete()
    calllll = call.data
    filial = calllll.upper()
    await state.finish()
    await call.message.answer(f'Tanlangan filial: <b>{filial}</b>')
    await call.message.answer(""""Guruhingizni kiriting ⬇️

✅ BG-1375
❌ bg1375""")
    await Bolimlar.guruh.set()


@dp.message_handler(content_types="text", state=Bolimlar.guruh)
async def get_orniga(message: types.Message, state: FSMContext):
    global teacher_group
    teacher_group = message.text
    await state.finish()
    await message.answer("""O’rningizga tayinlangan hodim ism va familyasini to’liq kiriting ⬇️

✅ <i>Bekbayev Sirojiddin</i>
❌ <i>Siroj</i>""")
    await Bolimlar.orniga_hodim.set()


@dp.message_handler(content_types="text", state=Bolimlar.orniga_hodim)
async def get_sabab(message: types.Message, state: FSMContext):
    global change_teacher
    change_teacher = message.text
    await state.finish()
    await message.answer("Javob so’rash sababini to’liq kiriting ⬇️")
    await Bolimlar.sabab.set()


@dp.message_handler(content_types="text", state=Bolimlar.sabab)
async def yuborildi(message: types.Message, state: FSMContext):
    sababi = message.text
    await save_data(teacher_user_id, teacher_name, teacher_time, filial, teacher_group, change_teacher, sababi)
    await state.finish()
