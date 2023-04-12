import logging
import os
import sqlite3
from sqlite3 import Error


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject


def create_teacher_table(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            subject TEXT
        )
    """)
    except Error as e:
        print(e)
    conn.commit()


def insert_teacher(conn, teacher):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO teacher (name, age, subject)
        VALUES (?, ?, ?)
    """, (teacher.name, teacher.age, teacher.subject))
    conn.commit()


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        create_teacher_table(conn)
        logger = logging.getLogger('proxy_generator')
        logger.info(
            'Database connection is successfully created.')
        teacher1 = Teacher('John', 35, 'Math')
        insert_teacher(conn, teacher1)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def define_database_name(db_name):
    # Windows
    if os.name == 'nt':
        return os.getcwd() + "\\" + db_name + ".db"
    # Posix
    return os.getcwd() + "/" + db_name + ".db"
