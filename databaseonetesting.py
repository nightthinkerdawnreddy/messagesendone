import sqlite3
#from .alert import email_alert
from datetime import datetime, time
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())
c.execute("SELECT * FROM main_mainmodule")
results = c.fetchall()
for i in results:
    print(i)