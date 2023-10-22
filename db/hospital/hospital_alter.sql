alter table sponsors
    add column organization bit(1),
    add column col3 int not null,
    add column col4 int not null default 91;


insert donations values (3, 15000000000, '2023-10-21', 1, 2);

-- ERROR: 1264 (22003): Out of range value for column 'amount' at row 1

alter table donations
    modify column amount decimal(15,2) not null;

-- Query OK, 2 rows affected (0.0894 sec)
-- Records: 2  Duplicates: 0  Warnings: 0

insert donations values (3, 15000000000, '2023-10-21', 1, 2);

-- Query OK, 1 row affected (0.1848 sec)


alter table donations
    rename column amount to sum;

-- ERROR: 3959 (HY000): Check constraint 'donations_chk_1' uses column 'amount', hence column cannot be dropped or renamed.


alter table donations
    drop check donations_chk_1,
    rename column amount to sum,
    add check (sum > 0);

-- Query OK, 3 rows affected (0.2595 sec)
-- Records: 3  Duplicates: 0  Warnings: 0
