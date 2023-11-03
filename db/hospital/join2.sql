select *
from departments
join wards
order by departments.id, wards.id;

-- +----+--------------------------------------+----+------+----------------+
-- | id | department                           | id | ward | departments_id |
-- +----+--------------------------------------+----+------+----------------+
-- |  1 | Отделение общей терапии              |  1 | ОТ-1 |              1 |
-- |  1 | Отделение общей терапии              |  2 | ОТ-2 |              1 |
-- |  1 | Отделение общей терапии              |  3 | ОТ-3 |              1 |
-- |  1 | Отделение общей терапии              |  4 | ОТ-4 |              1 |
-- |  1 | Отделение общей терапии              |  5 | Н-1  |              2 |
-- |  1 | Отделение общей терапии              |  6 | Н-2  |              2 |
-- |  1 | Отделение общей терапии              |  7 | Н-3  |              2 |
-- |  1 | Отделение общей терапии              |  8 | Н-4  |              2 |
-- |  1 | Отделение общей терапии              |  9 | Н-5  |              2 |
-- |  1 | Отделение общей терапии              | 10 | Н-6  |              2 |
-- |  1 | Отделение общей терапии              | 11 | Н-7  |              2 |
-- |  1 | Отделение общей терапии              | 12 | Н-8  |              2 |
-- |  1 | Отделение общей терапии              | 13 | К-1  |              3 |
-- |  1 | Отделение общей терапии              | 14 | К-2  |              3 |
-- |  1 | Отделение общей терапии              | 15 | К-3  |              3 |
-- |  1 | Отделение общей терапии              | 16 | К-4  |              3 |
-- |  1 | Отделение общей терапии              | 17 | К-5  |              3 |
-- |  1 | Отделение общей терапии              | 18 | К-6  |              3 |
-- |  1 | Отделение общей терапии              | 19 | К-7  |              3 |
-- |  1 | Отделение общей терапии              | 20 | К-8  |              3 |
-- |  1 | Отделение общей терапии              | 21 | К-9  |              3 |
-- |  1 | Отделение общей терапии              | 22 | ФД-1 |              4 |
-- |  1 | Отделение общей терапии              | 23 | ФД-2 |              4 |
-- |  1 | Отделение общей терапии              | 24 | ФД-3 |              4 |
-- |  1 | Отделение общей терапии              | 25 | ФД-4 |              4 |
-- |  1 | Отделение общей терапии              | 26 | ФД-5 |              4 |
-- |  1 | Отделение общей терапии              | 27 | Р-1  |              5 |
-- |  1 | Отделение общей терапии              | 28 | Р-2  |              5 |
-- |  1 | Отделение общей терапии              | 29 | Р-3  |              5 |
-- |  1 | Отделение общей терапии              | 30 | Р-4  |              5 |
-- |  1 | Отделение общей терапии              | 31 | Р-5  |              5 |
-- |  1 | Отделение общей терапии              | 32 | Т-1  |              6 |
-- |  1 | Отделение общей терапии              | 33 | Т-2  |              6 |
-- |  1 | Отделение общей терапии              | 34 | Т-3  |              6 |
-- |  1 | Отделение общей терапии              | 35 | Т-4  |              6 |
-- |  1 | Отделение общей терапии              | 36 | Т-5  |              6 |
-- |  1 | Отделение общей терапии              | 37 | Т-6  |              6 |
-- |  1 | Отделение общей терапии              | 38 | Т-7  |              6 |
-- |  1 | Отделение общей терапии              | 39 | Т-8  |              6 |
-- |  1 | Отделение общей терапии              | 40 | Т-9  |              6 |
-- |  1 | Отделение общей терапии              | 41 | ФТ-1 |              7 |
-- |  1 | Отделение общей терапии              | 42 | ФТ-2 |              7 |
-- |  1 | Отделение общей терапии              | 43 | ФТ-3 |              7 |
-- |  1 | Отделение общей терапии              | 44 | ФТ-4 |              7 |
-- |  1 | Отделение общей терапии              | 45 | ФТ-5 |              7 |
-- |  1 | Отделение общей терапии              | 46 | ФТ-6 |              7 |
-- |  1 | Отделение общей терапии              | 47 | ФТ-7 |              7 |
-- |  1 | Отделение общей терапии              | 48 | ФТ-8 |              7 |
-- |  1 | Отделение общей терапии              | 49 | ФТ-9 |              7 |
-- |  2 | Неврологическое отделение            |  1 | ОТ-1 |              1 |
-- |  2 | Неврологическое отделение            |  2 | ОТ-2 |              1 |
-- |  2 | Неврологическое отделение            |  3 | ОТ-3 |              1 |
-- |  2 | Неврологическое отделение            |  4 | ОТ-4 |              1 |
-- |  2 | Неврологическое отделение            |  5 | Н-1  |              2 |
-- ..........................................................................
-- +----+--------------------------------------+----+------+----------------+
-- 343 rows in set (0.0016 sec)


  select *
    from departments as d
    join wards as w
      on d.id = w.departments_id
order by d.id, w.id;

-- +----+--------------------------------------+----+------+----------------+
-- | id | department                           | id | ward | departments_id |
-- +----+--------------------------------------+----+------+----------------+
-- |  1 | Отделение общей терапии              |  1 | ОТ-1 |              1 |
-- |  1 | Отделение общей терапии              |  2 | ОТ-2 |              1 |
-- |  1 | Отделение общей терапии              |  3 | ОТ-3 |              1 |
-- |  1 | Отделение общей терапии              |  4 | ОТ-4 |              1 |
-- |  2 | Неврологическое отделение            |  5 | Н-1  |              2 |
-- |  2 | Неврологическое отделение            |  6 | Н-2  |              2 |
-- |  2 | Неврологическое отделение            |  7 | Н-3  |              2 |
-- |  2 | Неврологическое отделение            |  8 | Н-4  |              2 |
-- |  2 | Неврологическое отделение            |  9 | Н-5  |              2 |
-- |  2 | Неврологическое отделение            | 10 | Н-6  |              2 |
-- |  2 | Неврологическое отделение            | 11 | Н-7  |              2 |
-- |  2 | Неврологическое отделение            | 12 | Н-8  |              2 |
-- |  3 | Кардиологическое отделение           | 13 | К-1  |              3 |
-- |  3 | Кардиологическое отделение           | 14 | К-2  |              3 |
-- |  3 | Кардиологическое отделение           | 15 | К-3  |              3 |
-- |  3 | Кардиологическое отделение           | 16 | К-4  |              3 |
-- |  3 | Кардиологическое отделение           | 17 | К-5  |              3 |
-- |  3 | Кардиологическое отделение           | 18 | К-6  |              3 |
-- |  3 | Кардиологическое отделение           | 19 | К-7  |              3 |
-- |  3 | Кардиологическое отделение           | 20 | К-8  |              3 |
-- |  3 | Кардиологическое отделение           | 21 | К-9  |              3 |
-- |  4 | Отделение функциональной диагностики | 22 | ФД-1 |              4 |
-- |  4 | Отделение функциональной диагностики | 23 | ФД-2 |              4 |
-- |  4 | Отделение функциональной диагностики | 24 | ФД-3 |              4 |
-- |  4 | Отделение функциональной диагностики | 25 | ФД-4 |              4 |
-- |  4 | Отделение функциональной диагностики | 26 | ФД-5 |              4 |
-- |  5 | Реанимация и интенсивная терапия     | 27 | Р-1  |              5 |
-- |  5 | Реанимация и интенсивная терапия     | 28 | Р-2  |              5 |
-- |  5 | Реанимация и интенсивная терапия     | 29 | Р-3  |              5 |
-- |  5 | Реанимация и интенсивная терапия     | 30 | Р-4  |              5 |
-- |  5 | Реанимация и интенсивная терапия     | 31 | Р-5  |              5 |
-- |  6 | Токсикологическое отделение          | 32 | Т-1  |              6 |
-- |  6 | Токсикологическое отделение          | 33 | Т-2  |              6 |
-- |  6 | Токсикологическое отделение          | 34 | Т-3  |              6 |
-- |  6 | Токсикологическое отделение          | 35 | Т-4  |              6 |
-- |  6 | Токсикологическое отделение          | 36 | Т-5  |              6 |
-- |  6 | Токсикологическое отделение          | 37 | Т-6  |              6 |
-- |  6 | Токсикологическое отделение          | 38 | Т-7  |              6 |
-- |  6 | Токсикологическое отделение          | 39 | Т-8  |              6 |
-- |  6 | Токсикологическое отделение          | 40 | Т-9  |              6 |
-- |  7 | Физиотерапевтическое отделение       | 41 | ФТ-1 |              7 |
-- |  7 | Физиотерапевтическое отделение       | 42 | ФТ-2 |              7 |
-- |  7 | Физиотерапевтическое отделение       | 43 | ФТ-3 |              7 |
-- |  7 | Физиотерапевтическое отделение       | 44 | ФТ-4 |              7 |
-- |  7 | Физиотерапевтическое отделение       | 45 | ФТ-5 |              7 |
-- |  7 | Физиотерапевтическое отделение       | 46 | ФТ-6 |              7 |
-- |  7 | Физиотерапевтическое отделение       | 47 | ФТ-7 |              7 |
-- |  7 | Физиотерапевтическое отделение       | 48 | ФТ-8 |              7 |
-- |  7 | Физиотерапевтическое отделение       | 49 | ФТ-9 |              7 |
-- +----+--------------------------------------+----+------+----------------+
-- 49 rows in set (0.0008 sec)


  select department, ward
    from departments as d
    join wards as w
      on d.id = w.departments_id
order by d.id, w.id;

-- +--------------------------------------+------+
-- | department                           | ward |
-- +--------------------------------------+------+
-- | Отделение общей терапии              | ОТ-1 |
-- | Отделение общей терапии              | ОТ-2 |
-- | Отделение общей терапии              | ОТ-3 |
-- | Отделение общей терапии              | ОТ-4 |
-- | Неврологическое отделение            | Н-1  |
-- | Неврологическое отделение            | Н-2  |
-- | Неврологическое отделение            | Н-3  |
-- | Неврологическое отделение            | Н-4  |
-- | Неврологическое отделение            | Н-5  |
-- | Неврологическое отделение            | Н-6  |
-- | Неврологическое отделение            | Н-7  |
-- | Неврологическое отделение            | Н-8  |
-- | Кардиологическое отделение           | К-1  |
-- | Кардиологическое отделение           | К-2  |
-- | Кардиологическое отделение           | К-3  |
-- | Кардиологическое отделение           | К-4  |
-- | Кардиологическое отделение           | К-5  |
-- | Кардиологическое отделение           | К-6  |
-- | Кардиологическое отделение           | К-7  |
-- | Кардиологическое отделение           | К-8  |
-- | Кардиологическое отделение           | К-9  |
-- | Отделение функциональной диагностики | ФД-1 |
-- | Отделение функциональной диагностики | ФД-2 |
-- | Отделение функциональной диагностики | ФД-3 |
-- | Отделение функциональной диагностики | ФД-4 |
-- | Отделение функциональной диагностики | ФД-5 |
-- | Реанимация и интенсивная терапия     | Р-1  |
-- | Реанимация и интенсивная терапия     | Р-2  |
-- | Реанимация и интенсивная терапия     | Р-3  |
-- | Реанимация и интенсивная терапия     | Р-4  |
-- | Реанимация и интенсивная терапия     | Р-5  |
-- | Токсикологическое отделение          | Т-1  |
-- | Токсикологическое отделение          | Т-2  |
-- | Токсикологическое отделение          | Т-3  |
-- | Токсикологическое отделение          | Т-4  |
-- | Токсикологическое отделение          | Т-5  |
-- | Токсикологическое отделение          | Т-6  |
-- | Токсикологическое отделение          | Т-7  |
-- | Токсикологическое отделение          | Т-8  |
-- | Токсикологическое отделение          | Т-9  |
-- | Физиотерапевтическое отделение       | ФТ-1 |
-- | Физиотерапевтическое отделение       | ФТ-2 |
-- | Физиотерапевтическое отделение       | ФТ-3 |
-- | Физиотерапевтическое отделение       | ФТ-4 |
-- | Физиотерапевтическое отделение       | ФТ-5 |
-- | Физиотерапевтическое отделение       | ФТ-6 |
-- | Физиотерапевтическое отделение       | ФТ-7 |
-- | Физиотерапевтическое отделение       | ФТ-8 |
-- | Физиотерапевтическое отделение       | ФТ-9 |
-- +--------------------------------------+------+
-- 49 rows in set (0.0009 sec)
