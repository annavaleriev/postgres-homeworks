import csv

import psycopg2

connection = psycopg2.connect(host='Localhost', database='north', user='postgres', password='30051980')

try:
    with connection.cursor() as cursor:
        with open('north_data/customers_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                cursor.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                               (row[0], row[1], row[2]))
    connection.commit()

finally:
    connection.close()
