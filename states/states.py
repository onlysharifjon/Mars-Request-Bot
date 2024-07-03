from aiogram.dispatcher.filters.state import State,StatesGroup

class Bolimlar(StatesGroup):
    ism = State()
    filial = State()
    vaqt = State()
    guruh = State()
    orniga_hodim = State()
    sabab = State()

