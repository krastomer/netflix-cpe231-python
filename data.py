import sqlite3

def readSqliteTable(databases):
    try:
        sqliteConnection = sqlite3.connect(databases)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = "SELECT * from Staff"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print(records)
        print("Total rows are:  ", len(records))
        for row in records :
            for i in row :
                print(i)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def insertMultipleRecords(databases,recordList):
    try:
        sqliteConnection = sqlite3.connect(databases)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO staff
                          (id_staff , first_name , last_name , password , email , salary) 
                          VALUES (?, ?, ?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into SqliteDb_developers table")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
def main():
    databases = r'C:\Users\subta\Desktop\sqlite-amalgamation-3350500\DBNetflix\DBNetflix.db'
    recordList = [(2, 'EAK', 'JUNG', '159753', 'SADSADSAD@ASDSADAS.COM',1000)]
    insertMultipleRecords(databases, recordList)

if __name__ == '__main__':
    main()
