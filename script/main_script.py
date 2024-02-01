from pyrogram import Client
from pyrogram import types, filters

from aiogram import Bot

from DataBase.post_data import PostData
from DataBase.google_sheet import GoogleSheet
from DataBase.script_status import ScriptStatus


# from dotenv import load_dotenv
# import os
# load_dotenv()
# bot = Bot(token=os.getenv('BOT_TOKEN'))
                

app = Client(
        name='script/session/account',
        api_id='20901863',
        api_hash='ef8aac4e9dd76a731194c49a926e5728'
    )



@app.on_message(filters=(filters.channel | filters.group)) #реагирует когда юзер боту приходит сообщение
async def my_handler(app: app, message: types.Message):
    if ScriptStatus().get_status():
        try:
            chanel_list = ['bbbreaking' ,'rusbrief']

            url_in_ent = False

            if message.chat.username in chanel_list:
                
                try:
                    for entities in message.entities:
                        if entities.url != 'None':
                            if message.chat.username in entities.url:
                                url_in_ent = True
                except:
                    pass



                if url_in_ent:
                    await app.send_message('@pawettanews', message.text)
                else: 
                    await app.copy_message(
                            chat_id='@pawettanews',
                            from_chat_id=message.chat.username,
                            message_id=message.id,
                            reply_to_message_id = None,
                            )
                

                if message.text != None:
                    text_post = message.text
                    original_url = message.link
                    date_post = str(message.date).split(' ')[0]

                    PostData().Save_data_post_DB(text=text_post.replace('"', ''), link=original_url, date=date_post)
                    GoogleSheet().Save_in_google_sheets_DB(text=text_post, link=original_url, date=date_post)


                
                
        except Exception as ex:
            print(f'Что то пошло не так по время публикации записи - {ex}')
        





