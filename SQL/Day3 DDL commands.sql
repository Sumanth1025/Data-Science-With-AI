create database d22r;
use d22r;
create table students(student_id int, student_name varchar(50), marks int, email_id varchar(50));
alter table students add column phone_number int;
select * from students;
alter table students rename column phone_number to phone_no;
alter table students modify column marks int;
select * from students;
Insert into students values
(1,'sai',93,'sai@gmail.com',42354),
(2,'uma',65,'uma@gmail.com',12134);
DESC students;
CREATE TABLE students_new AS
SELECT DISTINCT *
FROM students;
SELECT * FROM students_new;
SHOW DATABASES;
use sakila;
SHOW tables;