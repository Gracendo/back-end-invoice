# import sqlite3
from models.constant import *


class Invoice:
    TABLE_NAME = "invoice"

    def __init__(self, invoice_id=None, product_id=None, datetime=None, total=None):
        self.invoice_id = invoice_id
        self.product_id = product_id
        self.datetime = datetime
        self.total = total

    def save(self):
        # conn = sqlite3.connect(PATH_TO_DB)
        cursor = conn.cursor()

        # Create table if not exists
        # cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (invoice_id INTEGER PRIMARY KEY,product_id INTEGER FOREIGN KEY datetime TEXT, total INTEGER)")

        # Insert or update record
        cursor.execute("INSERT OR REPLACE INTO {} (invoice_id, product_id, datetime, total) VALUES (?, ?, ?,?)".format(self.TABLE_NAME),
                       (self.invoice_id, self.product_id, self.datetime, self.total))

        conn.commit()
        # conn.close()

    @staticmethod
    def read():
        # conn = sqlite3.connect(PATH_TO_DB)
        cursor = conn.cursor()
        # print(conn.total_changes)

        # Read all records
        cursor.execute(f"SELECT * FROM {Invoice.TABLE_NAME}")
        # cursor.execute("SELECT * FROM product")
        records = cursor.fetchall()

        # conn.close()

        return records

    def delete(self):
        # conn = sqlite3.connect(PATH_TO_DB)
        cursor = conn.cursor()

        # Delete record by invoice_id
        cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE invoice_id = ?", (self.invoice_id,))

        conn.commit()














#import sqlite3

#class invoice:
    #TABLE_NAME="invoice"
    #def __init__(self, invoice_id=None, datetime=None, totalamount=None) -> None:
        #self.invoice_id=invoice_id
        #self.datetime = datetime
        #self.totalamount = totalamount
    #def save(self):
       # pass
    #def read():
        pass
    #def delete(self):
        #pass