import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

user = os.environ['user_db']
user = os.environ['password']






SQL_CREATE_DB = '''

'''

SQL_CREATE_TABLE = '''

'''

def execute_db(INSTRUCTION):
    con = psycopg2.connect(f"dbname=blog user={user} password={pswd}")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    try:
        cur.execute(INSTRUCTION)
    finally:
        con.close()
        cur.close()