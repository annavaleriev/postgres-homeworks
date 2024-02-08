import configparser
import csv


import psycopg2

from settings import CONFIG_PATH

# Чтение кофигурационного файла
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# Получение пароля для подключения к базе данных
DB_PASSWORD = config['database']['DB_PASSWORD']

# Установка соединения с базой данных. Psycopg2 - это библиотека для работы с базой данных PostgreSQL.
connection = psycopg2.connect(host='localhost', database='north', user='postgres', password=DB_PASSWORD)


def load_fixtures(file_path: str, table_name: str) -> None:
    """Метод, который загружает данные из CSV-файла в таблицу базы данных"""
    # Открытие курсора для взаимодействия с базой данных
    with connection.cursor() as cursor:
        # Открытие файла cvs с данными для чтения
        with open(file_path, 'r') as file:
            # Создание объекта DictReader, который позволяет читать CSV файл как словарь,
            # где ключами являются имена столбцов.
            reader = csv.DictReader(file)

            # Итерация по строкам в CSV файле
            for row in reader:
                # Создание строки с именами столбцов и строки с заполнителями %s для значений. %s здесь используется
                # как заполнитель для параметров, которые будут вставлены в запрос. Это защищает от SQL-инъекций
                # и обеспечивает безопасное выполнение запросов.
                columns = ', '.join(row.keys())
                values = ', '.join(['%s'] * len(row))
                # Формирование SQL запроса для вставки данных в таблицу table_name из CSV файла. ON CONFLICT DO NOTHING
                # - это часть SQL синтаксиса PostgreSQL, которая указывает базе данных не выполнять вставку,
                # если встречается конфликт (например, дубликат ключа)
                query = "INSERT INTO %s (%s) VALUES (%s) ON CONFLICT DO NOTHING" % (table_name, columns, values)

                # Выполнение SQL запроса с передачей значений в качестве параметров для вставки. row.values() содержит
                # значения для текущей строки CSV файла. tuple(row.values()) преобразует значения в кортеж,
                # который передается в качестве параметров в запрос.
                cursor.execute(query, tuple(row.values()))


# Загрузка данных из CSV файлов в таблицы базы данных
load_fixtures('north_data/customers_data.csv', "customers")
load_fixtures('north_data/employees_data.csv', "employees")
load_fixtures('north_data/orders_data.csv', "orders")


# Сохранение изменений в базе данных
connection.commit()
# Закрытие соединения с базой данных
connection.close()
