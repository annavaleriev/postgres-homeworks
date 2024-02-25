-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
create table student
(
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
);

-- 2. Добавить в таблицу student колонку middle_name varchar
alter table student add column middle_name varchar;

-- 3. Удалить колонку middle_name
alter table student drop column middle_name;

-- 4. Переименовать колонку birthday в birth_date
alter table student rename birthday to birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
alter table student alter column phone set data type varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
insert into student (first_name, last_name, birth_date, phone) values ('Anna', 'Ivanova', '15.03.1990', '79112225555');
insert into student (first_name, last_name, birth_date, phone) values ('Irina', 'Ivleeva', '16.05.1990', '7921111111');
insert into student (first_name, last_name, birth_date, phone) values ('Petr', 'Fadeev', '25.03.1989', '79111234455');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
truncate table student restart identity