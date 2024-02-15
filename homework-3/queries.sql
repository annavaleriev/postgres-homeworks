-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)

select c.company_name as customer, CONCAT(first_name, ' ', last_name) as employee
from orders o
join customers c using(customer_id)
join employees e using(employee_id)
join shippers s on o.ship_via = s.shipper_id
where c.city = 'London' and e.city = 'London' and s.company_name = 'United Package';

-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.

select p.product_name, p.units_in_stock, s.company_name, s.phone
from products p
join suppliers s using(supplier_id)
join categories c using(category_id)
where p.discontinued = 0 and p.units_in_stock < 25 and c.category_name in ('Dairy Products', 'Condiments')
order by p.units_in_stock;

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа

select c.company_name
from customers c
left join orders o using (customer_id)
where o.order_id is null;

-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.

select distinct product_name
from products p
where product_id = any (select product_id from order_details o where o.quantity = 10)