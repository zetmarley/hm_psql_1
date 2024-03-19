-- SQL-команды для создания таблиц

CREATE DATABASE north;

CREATE TABLE north_data
(
	employees varchar(100) NOT NULL,
	customers varchar(1000),
	orders varchar(1000)
);