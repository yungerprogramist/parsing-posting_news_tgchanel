import gspread




"""
https://docs.google.com/spreadsheets/d/1Q5njawnjf7CP3nlCsiz3kbwrjdXUwI8M8lhV-SWm2jg/edit#gid=0
столбцы: 1.дата  2.Нажатых старт  3.Посмотрел курсы
"""



class GoogleSheet:



    def __init__(self) -> None:
        """подключается к google sheets"""
        gc = gspread.service_account(filename='parsing-auto-posting-59567be80d81.json')
        sh  = gc.open("информация о пользователях")
        self.worksheet  = sh.worksheet("Лист2")



    def next_available_row(self) -> int:
        """Определяет последнюю строку в таблице"""
        str_list = list(filter(None, self.worksheet.col_values(1)))
        return str(len(str_list)+1)


    def Save_in_google_sheets_DB(self, text: str, link: str, date: str):
        """Заносит изменения в google таблицу"""
        try:
            worksheet = self.worksheet

            last_row  = self.next_available_row()
            id_row = int(last_row) -1 

            worksheet.update_acell("A{}".format(last_row), str(id_row)) #номер строки 
            worksheet.update_acell("B{}".format(last_row), text) #текст
            worksheet.update_acell("C{}".format(last_row), link) #сылка
            worksheet.update_acell("D{}".format(last_row), date) # дата
            # worksheet.update_acell("E{}".format(last_row), 'нет')
            
            return True 
        
        except Exception as ex:
            print(f'Error на стадии сохранения в google таблицу - {ex}')
            return False
        

async def clear_google_data_DB():
    """Удаляет все даннные из гугл табицы каждый понедельник"""
    try:
        gc = gspread.service_account(filename='parsing-auto-posting-59567be80d81.json')
        sh  = gc.open("информация о пользователях")
        worksheet  = sh.worksheet("Лист2")
        worksheet.clear()
        worksheet.update_acell("A{}".format(1), '№')
        worksheet.update_acell("B{}".format(1), 'Текст')
        worksheet.update_acell("C{}".format(1), 'Оригинал')
        worksheet.update_acell("D{}".format(1), 'Дата')
        # worksheet.update_acell("E{}".format(1), 'Успешно ушел в канал')

    except Exception as ex:
        print(f'Error на стадии удаления из google таблицы - {ex}')

