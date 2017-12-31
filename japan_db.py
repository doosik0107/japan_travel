import sqlite3

class japan_holiday:
    def __init__(self):
        connection = sqlite3.connect('osaka.db')
        cursor = connection.cursor()
        self.db = connection
        self.cur = self.db.cursor()

    def search_holiday(self):
        self.cur.execute("SELECT * FROM japan_holiday")



