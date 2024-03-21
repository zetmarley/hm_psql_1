-- SQL-команды для создания таблиц

CREATE DATABASE north;

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
    first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
    title text,
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id character varying(10) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id character varying(10) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date,
	ship_city varchar(100)
);