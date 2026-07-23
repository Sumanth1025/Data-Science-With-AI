create database d22r;
use d22r;
create table students(student_id int, student_name varchar(50), marks int, email_id varchar(50));

alter table students add column phone_number int;

alter table students rename column phone_number to phone_no;

alter table students modify column marks int;

Insert into students values
(1,'sai',93,'sai@gmail.com',42354),
(2,'uma',65,'uma@gmail.com',12134);

SET SQL_SAFE_UPDATES = 0;
update students_new set marks=100;


select * from students_new;

create table aa(Id int unique, Name varchar(20) primary key not null, village varchar(20) not null );














