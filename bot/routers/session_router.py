from aiogram import Router


from aiogram import  F, Bot
from aiogram.types import Message, CallbackQuery 
from aiogram.fsm.context import FSMContext

from bot import keyboard as kb
from DataBase.google_sheet import GoogleSheet as gs



router = Router()



@router.callback_query(F.data == 'open_session')
async def open_session(callback: CallbackQuery):
    pass


@router.callback_query(F.data == 'close_session')
async def close_session(callback: CallbackQuery):
    pass