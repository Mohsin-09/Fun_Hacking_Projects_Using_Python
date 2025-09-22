"""
26_prepared_sql.py
Shows how to use parameterized queries to avoid injection (sqlite3).
"""
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE t(x TEXT)")
c.execute("INSERT INTO t VALUES(?)", ("ok",))
user = "ok' OR '1'='1"
print("Result with param:", c.execute("SELECT * FROM t WHERE x=?", (user,)).fetchall())
