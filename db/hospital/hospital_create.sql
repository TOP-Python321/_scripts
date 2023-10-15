drop database if exists hospital;
create database hospital;
use hospital;


create table departments (
    id tinyint unsigned primary key auto_increment,
    department varchar(100) not null unique,
    
    -- явное указание имени объекта ограничения
    -- constraint departments_not_empty_name check (department <> "")
    
    -- автоматическое создание имени объекта ограничения
    check (department <> "")
);

create table wards (
    id mediumint unsigned primary key auto_increment,
    ward varchar(10) not null unique,
    departments_id tinyint unsigned not null,
    check (ward <> "")
);

create table specializations (
    id tinyint unsigned primary key auto_increment,
    specialization varchar(120) not null unique,
    check (specialization <> "")
);

create table doctors (
    id smallint unsigned primary key auto_increment,
    last_name varchar(100) not null,
    first_name varchar(100) not null,
    patr_name varchar(100) not null,
    -- от -999,999.99 до 999,999.99
    salary decimal(8,2) not null,
    premium decimal(8,2) not null default 0,
    check (last_name <> ""),
    check (first_name <> ""),
    check (patr_name <> ""),
    check (salary > 0),
    check (premium >= 0)
);

create table doctors_specializations (
    doctors_id smallint unsigned not null,
    specializations_id tinyint unsigned not null,
    primary key (doctors_id, specializations_id)
);

create table vacations (
    id mediumint unsigned primary key auto_increment,
    start_date date null,
    end_date date null,
    doctors_id smallint unsigned not null,
    check (end_date > start_date)
);

create table sponsors (
    id smallint unsigned primary key auto_increment,
    sponsor varchar(250) not null unique,
    check (sponsor <> "")
);

create table donations (
    id mediumint unsigned primary key auto_increment,
    -- от -999,999,999.99 до 999,999,999.99
    amount decimal(11,2) not null,
    date date not null default (curdate()),
    departments_id tinyint unsigned not null,
    sponsors_id smallint unsigned not null,
    check (amount > 0)
    -- невозможно в MySQL
    -- check (date <= curdate())
);

delimiter //
create trigger donations_check_date
before insert
on donations for each row
begin
    if new.date > curdate() then
        set new.date = curdate();
    end if;
end //
delimiter ;


alter table wards
    add foreign key (departments_id) references departments (id);

alter table doctors_specializations
    add foreign key (doctors_id) references doctors (id),
    add foreign key (specializations_id) references specializations (id);

alter table vacations
    add foreign key (doctors_id) references doctors (id);

alter table donations
    add foreign key (departments_id) references departments (id),
    add foreign key (sponsors_id) references sponsors (id);

