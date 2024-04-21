import os.path
import sqlite3
conn = sqlite3.connect("invoice.sqlite", check_same_thread=False)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, 'invoice.sqlite')