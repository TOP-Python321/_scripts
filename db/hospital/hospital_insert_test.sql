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


insert ignore into donations
    (amount, departments_id, sponsors_id, date)
values
    (10000.0, 1, 1, '2023-09-01'),
    (26000.0, 2, 1, '2022-05-07');
    -- вызовет срабатывание триггера
    -- (85000.0, 1, 2, '2023-11-01');

