import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    price REAL,
    rating REAL,
    duration INTEGER,
    marketing REAL,
    students REAL,
    revenue REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")