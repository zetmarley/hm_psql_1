"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

with psycopg2.connect(
    host = 'localhost',
    database = 'north',
    user = 'postgres',
    password = '13799731'
) as conn:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO north_data VALUES (%s, %s, %s)',
                        [('Dr Mary', 'Darth Vader, Donald Duck', '3'), ('Dr  Blum', 'Timon, Pumba', '10')])