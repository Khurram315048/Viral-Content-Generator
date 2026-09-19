import sqlite3
import os

DB_PATH="outputs/agent_memory.db"

def init_db():
    os.makedirs("outputs", exist_ok=True)
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            tone TEXT,
            output_type TEXT,
            full_content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)""")
    conn.commit()
    conn.close()

def save_interaction(topic:str,tone:str,output_type:str,full_content:str):
    init_db()
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute("""
        INSERT INTO memory(topic,tone,output_type,full_content)
        VALUES(?,?,?,?)""",(topic,tone,output_type,full_content))
    conn.commit()
    conn.close()

def get_past_interactions(limit:int=5):
    init_db()
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute("""SELECT topic,tone,output_type,full_content,timestamp FROM memory ORDER BY timestamp DESC LIMIT ?
    """,(limit,))
    rows=cursor.fetchall()
    conn.close()
    return rows