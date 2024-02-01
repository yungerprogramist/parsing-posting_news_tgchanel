

class ScriptStatus():


    
    def get_status(self) ->bool:
        """Получение статуса скрипта запущен/остановлен"""
        try:
            file = open('Database/status_script.txt')
            data = file.read()
            if data == 'True':
                return True
            else:
                return False

        except Exception as ex:
            print(f'Что то не так с файлом stautus_script{ex}')
            return False
        finally:
            file.close()
        
    def change_status_script(self, status: bool):
        """Изменение статуса скрипта"""
        try:
            file = open('Database/status_script.txt', 'w')
            
            if status == True:
                file.write('True')
            else:
                file.write('False')
            
        except Exception as ex:
            print(f'Что то не так с файлом stautus_script{ex}')
        finally:
            file.close()

