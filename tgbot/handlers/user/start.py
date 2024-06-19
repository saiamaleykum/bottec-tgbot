import django
import logging
from aiogram import types, Bot
from aiogram.fsm.context import FSMContext

import states
from keyboards.default.basic import main_keyboard
from db.asyncpg.users import add_user


async def start(
    msg: types.Message, 
    state: FSMContext, 
    db_logger: logging.Logger,
    user_model: django.db.models.base.ModelBase
):
    await state.clear()
    if msg.from_user is None:
        return
    await add_user(user_model, msg.from_user.id, msg.from_user.username, db_logger)
    await msg.answer(
        text="Спасибо за подписку!\nВыбери раздел из меню", 
        reply_markup=main_keyboard
    )
    await state.set_state(states.user.UserMainMenu.menu)
    
