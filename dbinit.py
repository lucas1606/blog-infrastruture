import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from posts import post_list

user = os.environ['user_db']
pswd = os.environ['password']


SQL_CREATE_DB = "CREATE DATABASE blog;"

BASH_CHECK_IF_DB = '''if [ "$( psql -tAc "SELECT 1 FROM pg_database WHERE datname='blog'" )" = '1' ]
then
    echo "True"
else
    echo "False"
fi'''


SQL_CREATE_TABLE = '''
            CREATE TABLE IF NOT EXISTS post(
                id SERIAL PRIMARY KEY,
                data DATE DEFAULT CURRENT_DATE,
                titulo VARCHAR(100) NOT NULL,
                texto TEXT,
                imagem VARCHAR(100));

CREATE TABLE IF NOT EXISTS usuario(
id SERIAL PRIMARY KEY,
nome VARCHAR(100) UNIQUE NOT NULL,
senha VARCHAR(30) NOT NULL);
                '''
SQL_FIRST_INSERTION =f'''
                INSERT INTO post(titulo, texto, imagem)
                 VALUES
                    ('{post_list[0].titulo}', '{post_list[0].texto}', '{post_list[0].imagem}'),
                    ('{post_list[1].titulo}', '{post_list[1].texto}', '{post_list[1].imagem}')
                 
                 ;'''


def check_if_db_exists():
    check = os.popen(BASH_CHECK_IF_DB)
    output = check.read()
    if output == 'True\n':
        pass
    elif output == 'False\n':
        con = psycopg2.connect(f"user={user} password={pswd}")
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        try:
            cur.execute(SQL_CREATE_DB)
        finally:
            con.close()
            cur.close()
        execute_db(SQL_CREATE_TABLE)
        execute_db(SQL_FIRST_INSERTION)


def execute_db(INSTRUCTION, query_posts = 0):
    con = psycopg2.connect(f"dbname=blog user={user} password={pswd}")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    try:
        cur.execute(INSTRUCTION)
        if query_posts == 1:
            return cur.fetchone()
        if query_posts > 1:
            return cur.fetchmany(query_posts)
    finally:
        con.close()
        cur.close()

try:
    check_if_db_exists()

finally:
    pass
