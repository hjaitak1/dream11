import sqlite3

db_file = "dream11.db"

def get_db_connection():
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS selections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            match_id INTEGER,
            player_ids TEXT,
            timestamp TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER,
            user_id INTEGER,
            total_score INTEGER,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()
