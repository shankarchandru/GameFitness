import mysql.connector
from mysql.connector import Error
def getexercisedetail(exercise):
    try:
        connection = mysql.connector.connect (
        host = "", database = "", user = "", password = ""
        )
        cursor = mySQLConnection.cursor(buffered=True)
        sql_select_query = """ select * from DATABASE where exercise = %s"""
        cursor.execute(sql_select_query, (exercise,))
        record = cursor.fetchall()

        for row in record:
            print("Exercise 1 = ", row[n])
            print("Exercise 2 = ", row[n+1])
            print("Exercise 3 = ", row[n+2])

    except mysql.connector.Error as error:
        print("failed to get record from SQL table: {}".format(error))

    finally:
        if (mySQLConnection.is_connected()):
            cursor.close()
            mySQLConnection.close()
            print("Connection closed")
