import sqlite3



class BaseDB:

    def __init__(self) -> None:
        db = sqlite3.connect('project.db') 
        self.sql = db.cursor()
        self.db = db 


    def create_post_data_db(self):
        self.sql.execute('''CREATE TABLE IF NOT EXISTS "post_data" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "text" TEXT UNIQUE,
            "link" TEXT UNIQUE,
            "date" TEXT
        )''')
        self.db.commit()
        self.sql.close()
        
        