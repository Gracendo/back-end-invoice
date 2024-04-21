import sqlite3
from typing import Self
from models.constant import *

class Order:
    TABLE_NAME = "orders"
    def __init__(self, order_id=None,  invoice_id=None)->None:
        self.order_id = order_id
        self.invoice_id = invoice_id

    def save(self):
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO {} (order_id, invoice_id) VALUES (?, ?)".format(self.TABLE_NAME),(self.order_id, self.invoice_id))
        conn.commit()

    @staticmethod
    def read():
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {Order.TABLE_NAME}")
        records = cursor.fetchall()

        return records
    def delete(self):
        # conn = sqlite3.connect(PATH_TO_DB)
        cursor = conn.cursor()

        # Delete record by invoice_id
        cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE order_id = ?", (self.order_id,))
        conn.commit()