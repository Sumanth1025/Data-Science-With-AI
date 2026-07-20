create database d22r;
use d22r;
create table students(student_id int, student_name varchar(50), marks float, email_id varchar(50));
alter table students add column phone_number int;
select * from students;
alter table students rename column phone_number to phone_no;
alter table students modify column marks int;
select * from students;