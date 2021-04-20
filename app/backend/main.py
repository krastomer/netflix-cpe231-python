import os
import psycopg2

DATABASE_URL = os.environ.get('DB_URL')

# def main():


def hello_db():
    conn = psycopg2.connect(
        DATABASE_URL, sslmode='require')  # connect database
    cur = conn.cursor()  # get cursor for type command
    cur.execute('select * from account;')
    records = cur.fetchall()
    print(records)
    conn.close()
    return records


if __name__ == '__main__':
    _ = hello_db()
