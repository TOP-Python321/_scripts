update departments 
    set department = 'ABCD';

-- ERROR: 1062 (23000): Duplicate entry 'ABCD' for key 'departments.department'


update doctors 
    set last_name = 'SURNAME', 
        first_name = 'FIRST', 
        patr_name = 'PATRONYMIC';

-- Query OK, 500 rows affected (0.0315 sec)


update doctors 
    set last_name = 'SURNAME', 
        first_name = 'FIRST', 
        patr_name = 'PATRONYMIC' 
    limit 10;

-- Query OK, 10 rows affected (0.1862 sec)



update doctors 
    set last_name = 'SURNAME', 
        first_name = 'FIRST', 
        patr_name = 'PATRONYMIC'
    order by salary 
    limit 10;

-- Query OK, 8 rows affected (0.0129 sec)


update doctors 
    set salary = 78240 
    where id = 17;

-- Query OK, 1 row affected (0.0120 sec)


update doctors 
    set premium = default 
    where id = 17;

-- Query OK, 1 row affected (0.1865 sec)
