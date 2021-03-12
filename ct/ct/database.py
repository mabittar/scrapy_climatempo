import sqlite3

conn = sqlite3.connect('clima.db')

#definindo o cursorr
cursor = conn.cursor()


cursor.execute(""" CREATE TABLE clima (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        weather_now_C INTEGER,
        felling INTEGER,
        wind VARCHAR,
        humidity VARCHAR,
        pressure INTEGER,
        url VARCHAR,
        register_at TEXT DEFAULT CURRENT_TIMESTAMP)
        """)

cursor.execute("""insert into clima values()  """)



#close DB connection
conn.close()