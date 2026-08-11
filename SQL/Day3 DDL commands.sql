use d22r;
show tables;
create table Directors(
-- primary key
director_id int primary key auto_increment
);
ALTER TABLE Directors
ADD name VARCHAR(50) NOT NULL,
ADD dob DATE,
ADD nationality VARCHAR(100),
ADD awards TEXT;


create table movies (
	-- primary key
	movie_id int primary key auto_increment,
    -- not null 
    title varchar(225) not null,
    release_year year not null,
    genre varchar(100) not null,
    -- default
    language varchar(50) default 'Telugu',
    duration_minutes int not null,
    rating decimal(3,1),
    director_id int,
    -- foreign key
    foreign key (director_id) REFERENCES Directors(director_id)
);


create table Actors(
-- primary key
actor_id int primary key auto_increment,
name varchar(225) not null,
dob date,
gender char(1),
nationality varchar(100),
debut_year year
);


create table Movie_cast(
movie_id int,
actor_id int,
role_name varchar(225),
screen_time_minutes int,
-- foreign key
foreign key (movie_id) references Movies(movie_id),
foreign key (actor_id) references Actors(actor_id),
-- primary key
primary key(movie_id,actor_id)
);


create table Box_office(
movie_id int, budget bigint,
box_office_collection bigint,
domestic_collection bigint,
international_collection bigint,
-- foreign key
foreign key(movie_id) references Movies(movie_id),
-- primary key
primary key(movie_id)
);


INSERT INTO Directors (name, dob, nationality, awards) VALUES
('S. S. Rajamouli', '1973-10-10', 'Indian', 'National Film Award'),
('Trivikram Srinivas', '1971-11-07', 'Indian', 'Filmfare Award'),
('Sukumar', '1970-01-11', 'Indian', 'SIIMA Award');


INSERT INTO Movies 
(title, release_year, genre, language, duration_minutes, rating, director_id) 
VALUES
('Baahubali', 2015, 'Action', 159, 8.2, 1),
('Ala Vaikunthapurramuloo', 2020, 'Drama',  165, 7.3, 2),
('Pushpa', 2021, 'Action', 'Telugu', 179, 7.6, 3);


INSERT INTO Actors 
(name, dob, gender, nationality, debut_year) 
VALUES
('Prabhas', '1979-10-23', 'M', 'Indian', 2002),
('Allu Arjun', '1982-04-08', 'M', 'Indian', 2003),
('Rashmika Mandanna', '1996-04-05', 'F', 'Indian', 2016);


INSERT INTO Movie_cast 
(movie_id, actor_id, role_name, screen_time_minutes) 
VALUES
(1, 1, 'Amarendra Baahubali', 140),
(2, 2, 'Bantu', 150),
(3, 2, 'Pushpa Raj', 160),
(3, 3, 'Srivalli', 120);


INSERT INTO Box_office 
(movie_id, budget, box_office_collection, domestic_collection, international_collection) 
VALUES
(1, 1800000000, 6500000000, 5000000000, 1500000000),
(2, 1000000000, 2600000000, 2000000000, 600000000),
(3, 2000000000, 3600000000, 2500000000, 1100000000);


select * from movies;
select * from Directors;
select * from Actors;
select * from Movie_cast;
select * from Box_office;

desc movies;
desc box_office;
SELECT s.movie_id,s.title,b.budget FROM Movies s LEFT JOIN Box_office b ON s.movie_id = b.movie_id;
select s.movie_id,s.budget,m.title from Movies m right join Box_office s on s.movie_id = m.movie_id;







