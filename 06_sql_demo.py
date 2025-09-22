"""
06_sql_demo.py
DO NOT expose this code directly to the network.
Demonstrates SQL injection with an unsafe example on local SQLite, and how to fix it using parameters.
Run locally and inspect the database file created (demo.db).
"""
import sqlite3, os

db = "demo.db"
if os.path.exists(db):
    os.remove(db)
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, bio TEXT)")
cur.execute("INSERT INTO users(username,bio) VALUES(?,?)", ("alice","nice"))
conn.commit()

# Unsafe query (vulnerable if user input used directly)
unsafe_input = "alice' OR '1'='1"
q = f"SELECT * FROM users WHERE username = '{unsafe_input}'"
print("Unsafe query:", q)
print("Unsafe result:", cur.execute(q).fetchall())

# Safe parameterized version
safe_input = "alice' OR '1'='1"
safe_res = cur.execute("SELECT * FROM users WHERE username = ?", (safe_input,)).fetchall()
print("Safe parameterized result:", safe_res)
conn.close()
