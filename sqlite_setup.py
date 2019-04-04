import sqlite3

db = sqlite3.connect("database")

cursor = db.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS apprentices(
    id INTEGER PRIMARY KEY,
    name TEXT,
    dob DATE,
    base_location TEXT)

""")

db.commit()