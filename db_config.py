import sqlite3

def get_connection():
    conn = sqlite3.connect('monitoria.db')
    conn.execute('PRAGMA foreign_keys = ON')
    return conn