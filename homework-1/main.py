import csv

import psycopg2
from psycopg2 import sql

connection = psycopg2.connect(host='Localhost', database='north', user='postgres', password='30051980')


# try:
#     with connection.cursor() as cursor:
#         with open('north_data/customers_data.csv', 'r') as file:
#             reader = csv.reader(file)
#             next(reader)
#
#             for row in reader:
#                 cursor.execute("INSERT INTO customers VALUES (%s, %s, %s)",
#                                (row[0], row[1], row[2]))
#     connection.commit()
#
# finally:
#     connection.close()


def load_data_to_table(table_name: str, file_path: str):
    """Метод для загрузки данных из csv в таблицу"""
    with connection.cursor() as cursor:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # пропускаем 1ю строчку

            for row in reader:
                # подготовка запроса для вставки данных
                insert_query = sql.SQL("INSERT INTO {} VALUES ({})").format(
                    sql.Identifier(table_name),
                    sql.SQL(', ').join(map(sql.Literal, row))
                )
                # выполнение запроса
                cursor.execute(insert_query)

    connection.commit()


# загрузка данных из csv в таблицы
load_data_to_table('employees', 'north_data/employees_data.csv')
load_data_to_table('orders', 'north_data/orders_data.csv')

connection.close()
