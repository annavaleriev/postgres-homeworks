-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id char(5) NOT NULL,
	company_name varchar(300) NOT NULL,
	contact_name varchar (300) NOT NULL
);


CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(200) NOT NULL,
	last_name varchar (200) NOT NULL,
	title varchar (300) NOT NULL,
	birth_date date,
	notes text
);

ALTER TABLE customers
ADD CONSTRAINT unique_customer_id UNIQUE (customer_id);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5) REFERENCES customers (customer_id) NOT NULL,
	employee_id int REFERENCES employees (employee_id) NOT NULL,
	order_date date,
	ship_city varchar (200) NOT NULL
);