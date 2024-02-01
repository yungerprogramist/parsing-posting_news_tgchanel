from DataBase.Baseclass import BaseDB
import sqlite3

class PostData(BaseDB):
    __name_table = 'post_data'


    def Save_data_post_DB(self, text: str, link: str, date: str) -> bool:
        """Сохраняет посты в базу данных """
        db = None
        try: 
            self.sql.execute(f'INSERT INTO {self.__name_table} (text, link, date) VALUES ("{text}", "{link}", "{date}")')
                
            return True
        
        except sqlite3.Error as ex:
            if db: self.db.rollback() 
            print (f'Упс что то пошло не так с базой данных - {ex}') 
            return False
        finally: 
            self.db.commit()
            if db: self.db.close()


