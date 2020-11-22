show databases;

create database datarep;

use datarep;

create table student ( id int NOT NULL AUTO_INCREMENT, name varchar(250), age int, PRIMARY KEY(id) );

show tables;

desc student;

insert into student (name, age) VALUES ("Joe", 56); 

SELECT * FROM student;

update student set name="Mary" where id= 1;

delete from student where id = 1;

create table book ( id int NOT NULL AUTO_INCREMENT, title varchar(250), author varchar(250), price int, PRIMARY KEY(id) );

insert into book (title, author, price) values ("Harry Potter", "JK Rowling", 300);

SELECT * FROM book;
