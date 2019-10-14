# got the program off of this website:
#https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

import sqlite3
from sqlite3 import Error

def create_connection("""put file name here"""):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print('error')
    return conn

  """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """

def select_all_tasks(conn):
    cur = conn.cursor():
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)

"""
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """

def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

   """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """

def main():
    database = r"PUT IN THE FILE HERE"

    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn, 1)

        print("2. Query all tasks")
        select_all_tasks(conn)

"""This main() function creates a connection to the database
 DATABASE and calls the functions to query all rows
 from the tasks table and select tasks with priority 1:"""
