create database library;
use library;

create table books (book varchar (150) primary key,
author varchar (150) not null,
price float default 10,
category varchar(100) not null,
code float not null,
status varchar (50) not null)

insert into books(book,author,price,category,code,status) values ('1984','George Orwell',20,'Fiction',5678,'Available'),
('A Brief History of Time','Stephen Hawking',10,'Non-Fiction',9087,'Unavailable'),
('Catch-22','Joseph Heller',25,'Fiction',2357,'Unavailable'),
('To Kill a Mocking Bird','Harper Lee',30,'Fiction',7489,'Unavailable'),
('Night','Elie Wiesal',25,'Non-Fiction',3450,'Available'),
('Blink','Malcolm Gladwell',40,'Non-Fiction',3728,'Available'),
('Ariel','Sylvia Plath',35,'Non-Fiction',9037,'Unavailable'),
('Invisible Man','Ralph Ellison',30,'Fiction',5345,'Unavailable'),
('In Cold Blood','Truman Capote',35,'Non-Fiction',4379,'Available');

select * from books;

create table user(first_name varchar (150) primary key,
last_name varchar(150) not null,
phone int not null,
email varchar(150) not null,
username varchar(150) not null,
password varchar(150) not null,
book1 varchar (150),
book2 varchar(150),
book3 varchar(150),
price int);

insert into user(first_name,last_name,phone,email,username,password) values ('x','y',0563456785,'xy@gmail.com','xydxb','nunu123');

select * from user;

create table employee(first_name varchar (150) primary key,
last_name varchar(150) not null,
phone int not null,
email varchar(150) not null,
username varchar(150) not null,
password varchar(150) not null,
designation varchar(100) not null,
salary int not null);

insert into employee(first_name,last_name,phone,email,username,password,designation,salary) values ('a','b',0582346789,'ab@gmail.com','ab7890','ab','Executive',20000);

select * from employee;

drop database library;