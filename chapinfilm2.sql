-- drop database chapinfilm;

-- create database chapinfilm;
-- use chapinfilm;

create table if not exists film (
film_id int auto_increment primary key,
name varchar(255) unique key not null,
alias varchar(255) default null,
version int default null,
year year default null,
duration int default null,    -- in minute
-- rating enum ('G','PG','PG-13','R','NC-17'),
rating varchar(32) default null,
copies int default 1,
medium char(20) default 'DVD'
) ENGINE=InnoDB;

create table if not exists filmaward(
film_id int,
award varchar(128),
primary key (film_id, award),
foreign key (film_id) references film(film_id) ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

create table if not exists filmlanguage(
film_id int,
language varchar(32),
category varchar(32),  -- {Language, ClosedCaption}
primary key (film_id, language, category),
foreign key (film_id) references film(film_id) ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

create table if not exists filmstaff(
film_id int,
role char(32) not null,  -- {Director, Cast}
name varchar(128) not null, 
primary key (film_id, role, name),
foreign key (film_id) references film(film_id) ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

create table if not exists filmgenre(
film_id int,
genre varchar(128) not null,
primary key (film_id, genre),
foreign key (film_id) references film(film_id) ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;


