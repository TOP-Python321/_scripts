delete from doctors 
    where id between 5 and 15;

-- ERROR: 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails 
-- (`hospital`.`specializations_doctors`, 
--  CONSTRAINT `specializations_doctors_ibfk_1` 
--  FOREIGN KEY (`doctors_id`) 
--  REFERENCES `doctors` (`id`))


alter table specializations_doctors
    drop constraint specializations_doctors_ibfk_1,
    add foreign key (doctors_id)
        references doctors (id)
        on delete cascade;

-- Query OK, 300 rows affected (0.0839 sec)


alter table vacations
    drop constraint vacations_ibfk_1,
    add foreign key (doctors_id)
        references doctors (id)
        on delete cascade;

-- Query OK, 719 rows affected (0.2906 sec)


delete from doctors 
    where id between 5 and 15;

-- Query OK, 11 rows affected (0.0151 sec)

select count(*) from specializations_doctors;
-- 291

select count(*) from vacations;
-- 708
