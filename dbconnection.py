import sqlite3



class Dbconnection:
    cat = []


    def disconnect(self):
        self.conn.close()

    def get_cat_from_db(self):
        self.conn = sqlite3.connect("wallet.db")
        cursor = self.conn.execute("SELECT id, name from categories")
        for row in cursor:
            self.cat.append(row[1])
        self.disconnect()

    def add_category(self, value):
        self.conn = sqlite3.connect("wallet.db")
        sql = ''' INSERT INTO categories(name)
              VALUES(?) '''
        cur = self.conn.cursor()
        cur.execute(sql,(value,))
        self.conn.commit()
        self.disconnect()
        self.cat.append(value)



    def get_categories(self):

        return self.cat

    