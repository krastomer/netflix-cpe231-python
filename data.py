import sqlite3
class CRUD:
    def __init__(self,recordList,databases):
        self.recordList = recordList
        self.databases = databases
    def show(self):
        print(self.recordList)
        print(self.databases)
    def readSqliteTable(self):
        try:
            sqliteConnection = sqlite3.connect(self.databases)
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
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def insertMultipleRecords(self):
        try:
            sqliteConnection = sqlite3.connect(self.databases)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sqlite_insert_query = """INSERT INTO staff
                            (id_staff , first_name , last_name , password , email , salary) 
                            VALUES (?, ?, ?, ?, ?, ?);"""
            cursor.executemany(sqlite_insert_query, self.recordList)
            sqliteConnection.commit()
            print("Total", cursor.rowcount, "Records inserted successfully into SqliteDb_developers table")
            sqliteConnection.commit()
        except sqlite3.Error as error:
            print("Failed to insert multiple records into sqlite table", error)
        finally:
            cursor.close()
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
    def updateRecords(self):
        try:
            sqliteConnection = sqlite3.connect(self.databases)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            print("Before updating a record ")
            sql_select_query = """select * from Staff where id_staff = 1"""
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            sql_update_query = """Update Staff set salary = 7000 where id_staff = 1"""
            cursor.execute(sql_update_query)
            sqliteConnection.commit()
            print("Record Updated successfully ")
            print("After updating record ")
            record = cursor.fetchall()
            print(record)
        except sqlite3.Error as error:
            print("Failed to Update records into sqlite table", error)
        finally:
            cursor.close()
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
    def DeleteRecords(self):
        try:
            sqliteConnection = sqlite3.connect(self.databases)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql_select_query = """select * from Staff"""
            cursor.execute(sql_select_query)
            record = cursor.fetchall()
            print(record)

            # Delete a record
            sql_Delete_query = """Delete from Staff where id_Staff = 2"""
            cursor.execute(sql_Delete_query)
            sqliteConnection.commit()

            # Verify using select query (optional)
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            if len(records) == 0:
                print("Record Deleted successfully ")
        except sqlite3.Error as error:
            print("Failed to Delete records sqlite table", error)
        finally:
            cursor.close()
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
def main():
    databases = r'DBNetflix.db'
    a = CRUD([],databases)
    a.DeleteRecords()
if __name__ == '__main__':
    main()
