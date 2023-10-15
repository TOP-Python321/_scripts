insert into departments
    (department)
values
    ('отделение хирургии'),
    ('отделение офтальмологии');


insert into sponsors
    (sponsor)
values
    ('спонсор 1'),
    ('спонсор 2');


insert into donations
    (amount, date, departments_id, sponsors_id)
values
    (10000.0, '2023-09-01', 1, 1),
    (85000.0, '2023-11-01', 1, 2);

