from aiogram import Router


from aiogram import  F, Bot
from aiogram.types import Message, CallbackQuery 
from aiogram.fsm.context import FSMContext

from bot import keyboard as kb
from DataBase.script_status import ScriptStatus
from DataBase.google_sheet import GoogleSheet as gs



router = Router()


@router.message(F.text == '/start')
async def start(message: Message):
    name = message.from_user.username
    await message.answer(text=f'Добро пожаловать {name}', reply_markup=kb.start_kb)




@router.callback_query(F.data == 'main_menu')
async def go_work(callback: CallbackQuery):
    status_script = ScriptStatus().get_status()
    status_text = 'Запущен' if status_script else 'Приостановлен'  
    await callback.message.answer(text=f'Состояние скрипта: {status_text} \nВыберите действие', reply_markup=kb.main_menu)




@router.callback_query(F.data == 'work')
async def work(callback: CallbackQuery):
    status_script = ScriptStatus().get_status()
    status_text = 'Запущен' if status_script else 'Приостановлен'  
    await callback.message.answer(text=f'Состояние скрипта: {status_text} \nВыберите действие', reply_markup=kb.work_script)



@router.callback_query(F.data == 'go_work')
async def go_work(callback: CallbackQuery):
    ScriptStatus().change_status_script(status=True)
    await callback.message.answer(text='Скрипт успешно запущен', reply_markup=kb.start_kb)



@router.callback_query(F.data == 'stop_work')
async def stop_work(callback: CallbackQuery):
    ScriptStatus().change_status_script(status=False)
    await callback.message.answer(text='Скрипт успешно отсановил свою работу', reply_markup=kb.start_kb)




@router.callback_query(F.data == 'in_progres')
async def in_progres(callback: CallbackQuery):
    await callback.message.answer(text='Функция не существует, но она может появиться по вашему желанию', reply_markup=kb.start_kb)
