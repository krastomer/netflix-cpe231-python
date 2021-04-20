import os
import psycopg2

DATABASE_URL = os.environ['DB_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
cur.execute('select * from account;')
records = cur.fetchall()
print('done')
conn.close()
