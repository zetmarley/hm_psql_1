"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

"""Создаем списки кортежей для БД"""
customers = []
employees = []
orders = []

"""Извлекаем данные CSV в списки"""
with open('../homework-1/north_data/customers_data.csv', newline='') as csvfile:
    customers_reader = csv.reader(csvfile)
    for i in customers_reader:
        customers.append(tuple(i))
customers = customers[1::]

with open('../homework-1/north_data/employees_data.csv', newline='') as csvfile:
    employees_reader = csv.reader(csvfile)
    for i in employees_reader:
        employees.append(tuple(i))
employees = employees[1::]

with open('../homework-1/north_data/orders_data.csv', newline='') as csvfile:
    orders_reader = csv.reader(csvfile)
    for i in orders_reader:
        orders.append(tuple(i))
orders = orders[1::]

"""Вносим списки с данными в БД"""
with psycopg2.connect(
    host = 'localhost',
    database = 'north',
    user = 'postgres',
    password = '13799731'
) as conn:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', customers)
        cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', employees)
        cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', orders)