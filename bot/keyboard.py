from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton , ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder




start_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Меню', callback_data='main_menu')]])



main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Запуск/Стоп', callback_data='work')],
    [InlineKeyboardButton(text='Статистика', callback_data='in_progres')],
    [InlineKeyboardButton(text='Основной канал', callback_data='in_progres')],
    [InlineKeyboardButton(text='Добавление\Удаление каналов', callback_data='in_progres')],
    [InlineKeyboardButton(text='Логирование-отчетность', callback_data='in_progres')],
    
    # [InlineKeyboardButton(text='Открыть сессию', callback_data='open_session')],
    # [InlineKeyboardButton(text='закрыть сессию', callback_data='close_session')]
    ])

work_script = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Запустить', callback_data='go_work')],
    [InlineKeyboardButton(text='Остановить', callback_data='stop_work')],
    [InlineKeyboardButton(text='В меню', callback_data='main_menu')]
    ])