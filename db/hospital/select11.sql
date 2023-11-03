select ward, departments_id 
  from wards;

-- +------+----------------+
-- | ward | departments_id |
-- +------+----------------+
-- | ОТ-1 |              1 |
-- | ОТ-2 |              1 |
-- | ОТ-3 |              1 |
-- | ОТ-4 |              1 |
-- | Н-1  |              2 |
-- | Н-2  |              2 |
-- | Н-3  |              2 |
-- | Н-4  |              2 |
-- | Н-5  |              2 |
-- | Н-6  |              2 |
-- | Н-7  |              2 |
-- | Н-8  |              2 |
-- | К-1  |              3 |
-- | К-2  |              3 |
-- | К-3  |              3 |
-- | К-4  |              3 |
-- | К-5  |              3 |
-- | К-6  |              3 |
-- | К-7  |              3 |
-- | К-8  |              3 |
-- | К-9  |              3 |
-- | ФД-1 |              4 |
-- | ФД-2 |              4 |
-- | ФД-3 |              4 |
-- | ФД-4 |              4 |
-- | ФД-5 |              4 |
-- | Р-1  |              5 |
-- | Р-2  |              5 |
-- | Р-3  |              5 |
-- | Р-4  |              5 |
-- | Р-5  |              5 |
-- | Т-1  |              6 |
-- | Т-2  |              6 |
-- | Т-3  |              6 |
-- | Т-4  |              6 |
-- | Т-5  |              6 |
-- | Т-6  |              6 |
-- | Т-7  |              6 |
-- | Т-8  |              6 |
-- | Т-9  |              6 |
-- | ФТ-1 |              7 |
-- | ФТ-2 |              7 |
-- | ФТ-3 |              7 |
-- | ФТ-4 |              7 |
-- | ФТ-5 |              7 |
-- | ФТ-6 |              7 |
-- | ФТ-7 |              7 |
-- | ФТ-8 |              7 |
-- | ФТ-9 |              7 |
-- +------+----------------+
-- 49 rows in set (0.0057 sec)


select group_concat(ward separator ' ')
  from wards;

-- | group_concat(ward separator ' ') |
-- | К-1 К-2 К-3 К-4 К-5 К-6 К-7 К-8 К-9 Н-1 Н-2 Н-3 Н-4 Н-5 Н-6 Н-7 Н-8 ОТ-1 ОТ-2 ОТ-3 ОТ-4 Р-1 Р-2 Р-3 Р-4 Р-5 Т-1 Т-2 Т-3 Т-4 Т-5 Т-6 Т-7 Т-8 Т-9 ФД-1 ФД-2 ФД-3 ФД-4 ФД-5 ФТ-1 ФТ-2 ФТ-3 ФТ-4 ФТ-5 ФТ-6 ФТ-7 ФТ-8 ФТ-9 |
-- 1 row in set (0.0008 sec)


select 
  group_concat(ward separator ' '), 
  departments_id
from wards
group by departments_id;

-- +----------------------------------------------+----------------+
-- | group_concat(ward separator ' ')             | departments_id |
-- +----------------------------------------------+----------------+
-- | ОТ-1 ОТ-2 ОТ-3 ОТ-4                          |              1 |
-- | Н-1 Н-2 Н-3 Н-4 Н-5 Н-6 Н-7 Н-8              |              2 |
-- | К-1 К-2 К-3 К-4 К-5 К-6 К-7 К-8 К-9          |              3 |
-- | ФД-1 ФД-2 ФД-3 ФД-4 ФД-5                     |              4 |
-- | Р-1 Р-2 Р-3 Р-4 Р-5                          |              5 |
-- | Т-1 Т-2 Т-3 Т-4 Т-5 Т-6 Т-7 Т-8 Т-9          |              6 |
-- | ФТ-1 ФТ-2 ФТ-3 ФТ-4 ФТ-5 ФТ-6 ФТ-7 ФТ-8 ФТ-9 |              7 |
-- +----------------------------------------------+----------------+
-- 7 rows in set (0.0009 sec)


select 
  departments_id, 
  amount
from donations
order by departments_id;

-- +----------------+------------+
-- | departments_id | amount     |
-- +----------------+------------+
-- |              1 | 1978306.00 |
-- |              1 | 1178937.00 |
-- |              1 |  749144.00 |
-- |              2 |   34539.00 |
-- |              2 | 1068710.00 |
-- |              2 |  749196.00 |
-- |              2 |  582378.00 |
-- |              2 | 1458650.00 |
-- |              2 | 1749319.00 |
-- |              2 |  361385.00 |
-- |              2 | 1622961.00 |
-- |              2 | 1736411.00 |
-- |              2 | 1609155.00 |
-- |              2 |  245080.00 |
-- |              2 | 1975012.00 |
-- |              2 |  962637.00 |
-- |              2 |  669379.00 |
-- |              3 |  772941.00 |
-- |              3 |  480300.00 |
-- |              3 |  206213.00 |
-- |              3 |  957355.00 |
-- |              3 | 1450246.00 |
-- |              3 |  682265.00 |
-- |              3 |  780396.00 |
-- |              4 | 1164363.00 |
-- |              4 |  406599.00 |
-- |              4 | 1078535.00 |
-- |              4 | 1856049.00 |
-- |              4 |   71189.00 |
-- |              4 | 1870133.00 |
-- |              4 |  930587.00 |
-- |              4 | 1970821.00 |
-- |              4 | 1353578.00 |
-- |              4 | 1069726.00 |
-- |              4 |  803356.00 |
-- |              4 |  977319.00 |
-- |              4 |  913410.00 |
-- |              4 | 1938799.00 |
-- |              4 |  663411.00 |
-- |              4 |  473715.00 |
-- |              5 |  970906.00 |
-- |              5 | 1849157.00 |
-- |              5 |  837864.00 |
-- |              5 |  758834.00 |
-- |              5 |  590114.00 |
-- |              5 | 1895232.00 |
-- |              5 |  685092.00 |
-- |              5 |  995811.00 |
-- |              5 |  233839.00 |
-- |              5 | 1996781.00 |
-- |              5 |  685164.00 |
-- |              5 | 1588752.00 |
-- |              5 | 1629290.00 |
-- |              5 | 1843308.00 |
-- |              5 | 1672141.00 |
-- |              5 |  602358.00 |
-- |              6 | 1580363.00 |
-- |              6 |   85473.00 |
-- |              6 | 1452917.00 |
-- |              6 |  359862.00 |
-- |              6 |  388077.00 |
-- |              6 | 1783200.00 |
-- |              6 |  947229.00 |
-- |              6 | 1862822.00 |
-- |              6 |  472305.00 |
-- |              7 |  127413.00 |
-- |              7 |  637535.00 |
-- |              7 |  322365.00 |
-- |              7 |  735002.00 |
-- |              7 | 1466515.00 |
-- +----------------+------------+
-- 70 rows in set (0.0007 sec)


select 
  departments_id, 
  sum(amount)
from donations
group by departments_id;

-- +----------------+-------------+
-- | departments_id | sum(amount) |
-- +----------------+-------------+
-- |              1 |  3906387.00 |
-- |              2 | 14824812.00 |
-- |              3 |  5329716.00 |
-- |              4 | 17541590.00 |
-- |              5 | 18834643.00 |
-- |              6 |  8932248.00 |
-- |              7 |  3288830.00 |
-- +----------------+-------------+
-- 7 rows in set (0.0025 sec)


select 
  year(date) as `year`,
  amount
from donations
order by `year`;

-- +------+------------+
-- | year | amount     |
-- +------+------------+
-- | 2000 | 1862822.00 |
-- | 2001 |  780396.00 |
-- | 2001 |  637535.00 |
-- | 2001 |  473715.00 |
-- | 2002 |  772941.00 |
-- | 2003 | 1588752.00 |
-- | 2003 | 1978306.00 |
-- | 2003 |  803356.00 |
-- | 2004 |  590114.00 |
-- | 2004 |  685164.00 |
-- | 2004 | 1783200.00 |
-- | 2004 |  245080.00 |
-- | 2005 | 1164363.00 |
-- | 2005 | 1629290.00 |
-- | 2006 |  837864.00 |
-- | 2006 |   71189.00 |
-- | 2006 |  206213.00 |
-- | 2006 |  957355.00 |
-- | 2006 |  669379.00 |
-- | 2007 |  977319.00 |
-- | 2007 |  685092.00 |
-- | 2007 | 1580363.00 |
-- | 2007 | 1622961.00 |
-- | 2007 |  472305.00 |
-- | 2008 | 1996781.00 |
-- | 2008 |   34539.00 |
-- | 2009 | 1849157.00 |
-- | 2009 |  682265.00 |
-- | 2009 | 1749319.00 |
-- | 2011 |  361385.00 |
-- | 2011 |  735002.00 |
-- | 2012 |  758834.00 |
-- | 2012 |  602358.00 |
-- | 2012 | 1353578.00 |
-- | 2012 | 1736411.00 |
-- | 2012 |  970906.00 |
-- | 2012 | 1970821.00 |
-- | 2012 |  995811.00 |
-- | 2013 |  930587.00 |
-- | 2013 | 1672141.00 |
-- | 2014 |  406599.00 |
-- | 2014 |  359862.00 |
-- | 2014 | 1452917.00 |
-- | 2014 | 1450246.00 |
-- | 2014 | 1178937.00 |
-- | 2015 | 1609155.00 |
-- | 2016 | 1843308.00 |
-- | 2017 |  749196.00 |
-- | 2017 | 1895232.00 |
-- | 2017 |  749144.00 |
-- | 2018 |  127413.00 |
-- | 2018 |  962637.00 |
-- | 2018 |  388077.00 |
-- | 2018 |  947229.00 |
-- | 2019 | 1068710.00 |
-- | 2019 |  480300.00 |
-- | 2019 |   85473.00 |
-- | 2019 | 1458650.00 |
-- | 2020 | 1466515.00 |
-- | 2020 |  233839.00 |
-- | 2020 |  663411.00 |
-- | 2021 |  582378.00 |
-- | 2021 | 1069726.00 |
-- | 2021 | 1870133.00 |
-- | 2022 | 1856049.00 |
-- | 2022 | 1975012.00 |
-- | 2023 | 1078535.00 |
-- | 2023 | 1938799.00 |
-- | 2023 |  913410.00 |
-- | 2023 |  322365.00 |
-- +------+------------+
-- 70 rows in set (0.0006 sec)


select 
  year(date) as `year`,
  sum(amount)
from donations
group by `year`
order by `year`;

-- +------+-------------+
-- | year | sum(amount) |
-- +------+-------------+
-- | 2000 |  1862822.00 |
-- | 2001 |  1891646.00 |
-- | 2002 |   772941.00 |
-- | 2003 |  4370414.00 |
-- | 2004 |  3303558.00 |
-- | 2005 |  2793653.00 |
-- | 2006 |  2742000.00 |
-- | 2007 |  5338040.00 |
-- | 2008 |  2031320.00 |
-- | 2009 |  4280741.00 |
-- | 2011 |  1096387.00 |
-- | 2012 |  8388719.00 |
-- | 2013 |  2602728.00 |
-- | 2014 |  4848561.00 |
-- | 2015 |  1609155.00 |
-- | 2016 |  1843308.00 |
-- | 2017 |  3393572.00 |
-- | 2018 |  2425356.00 |
-- | 2019 |  3093133.00 |
-- | 2020 |  2363765.00 |
-- | 2021 |  3522237.00 |
-- | 2022 |  3831061.00 |
-- | 2023 |  4253109.00 |
-- +------+-------------+
-- 23 rows in set (0.0009 sec)


select
  if(salary > 75000, 'выше 75к', 'ниже 75к') as `cond`,
  salary
from doctors
order by salary;

-- +----------+-----------+
-- | cond     | salary    |
-- +----------+-----------+
-- | ниже 75к |  31408.00 |
-- | ниже 75к |  32721.00 |
-- | ниже 75к |  33689.00 |
-- | ниже 75к |  34788.00 |
-- | ниже 75к |  35524.00 |
-- | ниже 75к |  35830.00 |
-- | ниже 75к |  40564.00 |
-- | ниже 75к |  41278.00 |
-- | ниже 75к |  41474.00 |
-- | ниже 75к |  42030.00 |
-- | ниже 75к |  42676.00 |
-- | ниже 75к |  43388.00 |
-- | ниже 75к |  43597.00 |
-- | ниже 75к |  45166.00 |
-- | ниже 75к |  45493.00 |
-- | ниже 75к |  46621.00 |
-- | ниже 75к |  49330.00 |
-- | ниже 75к |  50036.00 |
-- | ниже 75к |  51046.00 |
-- | ниже 75к |  51634.00 |
-- | ниже 75к |  53314.00 |
-- | ниже 75к |  53752.00 |
-- | ниже 75к |  55059.00 |
-- | ниже 75к |  55731.00 |
-- | ниже 75к |  56007.00 |
-- | ниже 75к |  56665.00 |
-- | ниже 75к |  57498.00 |
-- | ниже 75к |  58077.00 |
-- | ниже 75к |  58463.00 |
-- | ниже 75к |  59637.00 |
-- | ниже 75к |  61477.00 |
-- | ниже 75к |  63626.00 |
-- | ниже 75к |  64267.00 |
-- | ниже 75к |  66624.00 |
-- | ниже 75к |  68228.00 |
-- | ниже 75к |  68419.00 |
-- | ниже 75к |  73389.00 |
-- | выше 75к |  75003.00 |
-- | выше 75к |  76232.00 |
-- | выше 75к |  76837.00 |
-- | выше 75к |  80145.00 |
-- | выше 75к |  80562.00 |
-- | выше 75к |  80645.00 |
-- | выше 75к |  80941.00 |
-- | выше 75к |  83075.00 |
-- | выше 75к |  86371.00 |
-- | выше 75к |  88402.00 |
-- | выше 75к |  89108.00 |
-- | выше 75к |  89440.00 |
-- | выше 75к |  91884.00 |
-- | выше 75к |  93215.00 |
-- | выше 75к |  97894.00 |
-- | выше 75к |  97945.00 |
-- | выше 75к |  99801.00 |
-- | выше 75к | 100450.00 |
-- | выше 75к | 100680.00 |
-- | выше 75к | 102468.00 |
-- | выше 75к | 103594.00 |
-- | выше 75к | 103977.00 |
-- | выше 75к | 105845.00 |
-- | выше 75к | 105903.00 |
-- | выше 75к | 107881.00 |
-- | выше 75к | 111419.00 |
-- | выше 75к | 113051.00 |
-- | выше 75к | 114117.00 |
-- | выше 75к | 115851.00 |
-- | выше 75к | 116222.00 |
-- | выше 75к | 117321.00 |
-- | выше 75к | 118941.00 |
-- | выше 75к | 119991.00 |
-- +----------+-----------+
-- 70 rows in set (0.0006 sec)


select
  if(salary > 75000, 'выше 75к', 'ниже 75к') as `cond`,
  count(salary) as 'кол-во',
  round(avg(salary)) as 'средний оклад'
from doctors
group by `cond`;

-- +----------+--------+---------------+
-- | cond     | кол-во | средний оклад |
-- +----------+--------+---------------+
-- | ниже 75к |     37 |         50501 |
-- | выше 75к |     33 |         97734 |
-- +----------+--------+---------------+
-- 2 rows in set (0.0029 sec)


update doctors
set premium = default
order by first_name
limit 30;

-- Query OK, 30 rows affected (0.0136 sec)
-- Rows matched: 30  Changed: 30  Warnings: 0


select
  concat_ws(' ', last_name, first_name, patr_name) as `ФИО`,
  if(salary > 75000, 'выше 75к', 'ниже 75к') as `уровень оклада`,
  if(premium > 0, 'есть', 'нет') as `премия`
from doctors
order by `уровень оклада` desc, `премия` desc, `ФИО`;

-- +-----------------------------------+----------------+--------+
-- | ФИО                               | уровень оклада | премия |
-- +-----------------------------------+----------------+--------+
-- | Васильева Александра Владимировна | ниже 75к       | нет    |
-- | Васильева Вероника Артёмовна      | ниже 75к       | нет    |
-- | Егорова Алёна Артёмовна           | ниже 75к       | нет    |
-- | Ершова Алиса Александровна        | ниже 75к       | нет    |
-- | Комаров Дмитрий Тимофеевич        | ниже 75к       | нет    |
-- | Коновалова Василиса Данииловна    | ниже 75к       | нет    |
-- | Кузин Даниил Миронович            | ниже 75к       | нет    |
-- | Кузнецова Вероника Ярославовна    | ниже 75к       | нет    |
-- | Лебедева Ева Дмитриевна           | ниже 75к       | нет    |
-- | Леонтьев Алексей Константинович   | ниже 75к       | нет    |
-- | Максимова Алиса Данииловна        | ниже 75к       | нет    |
-- | Малахов Глеб Иванович             | ниже 75к       | нет    |
-- | Миронова Алина Ильинична          | ниже 75к       | нет    |
-- | Михайлова Александра Даниэльевна  | ниже 75к       | нет    |
-- | Русаков Владимир Ильич            | ниже 75к       | нет    |
-- | Сорокин Богдан Степанович         | ниже 75к       | нет    |
-- | Андреева Елизавета Денисовна      | ниже 75к       | есть   |
-- | Афанасьев Иван Адамович           | ниже 75к       | есть   |
-- | Баранова Ярослава Никитична       | ниже 75к       | есть   |
-- | Белов Марк Даниилович             | ниже 75к       | есть   |
-- | Богданов Михаил Александрович     | ниже 75к       | есть   |
-- | Воронина Елизавета Сергеевна      | ниже 75к       | есть   |
-- | Горюнов Николай Миронович         | ниже 75к       | есть   |
-- | Гусева Любовь Тимофеевна          | ниже 75к       | есть   |
-- | Дьяконова Екатерина Михайловна    | ниже 75к       | есть   |
-- | Копылова Ульяна Кирилловна        | ниже 75к       | есть   |
-- | Леонова Татьяна Александровна     | ниже 75к       | есть   |
-- | Лобанова Евгения Антоновна        | ниже 75к       | есть   |
-- | Лопатин Марк Даниилович           | ниже 75к       | есть   |
-- | Парфенова Ева Евгеньевна          | ниже 75к       | есть   |
-- | Пахомов Марк Михайлович           | ниже 75к       | есть   |
-- | Семенова Полина Владиславовна     | ниже 75к       | есть   |
-- | Сухарева Элина Ярославовна        | ниже 75к       | есть   |
-- | Уткин Тимофей Максимович          | ниже 75к       | есть   |
-- | Фомин Константин Андреевич        | ниже 75к       | есть   |
-- | Шишкина Ксения Матвеевна          | ниже 75к       | есть   |
-- | Яковлев Иван Константинович       | ниже 75к       | есть   |
-- | Андреев Арсений Данилович         | выше 75к       | нет    |
-- | Астахова Альбина Максимовна       | выше 75к       | нет    |
-- | Горбачев Дмитрий Александрович    | выше 75к       | нет    |
-- | Долгов Артём Германович           | выше 75к       | нет    |
-- | Журавлева Аделина Степановна      | выше 75к       | нет    |
-- | Леонтьева Василиса Львовна        | выше 75к       | нет    |
-- | Малышева Арина Святославовна      | выше 75к       | нет    |
-- | Романова Анна Владимировна        | выше 75к       | нет    |
-- | Румянцева Вера Александровна      | выше 75к       | нет    |
-- | Соколов Андрей Фёдорович          | выше 75к       | нет    |
-- | Степанова Александра Денисовна    | выше 75к       | нет    |
-- | Фокин Владимир Артёмович          | выше 75к       | нет    |
-- | Фролов Даниил Давидович           | выше 75к       | нет    |
-- | Шмелева Анна Дмитриевна           | выше 75к       | нет    |
-- | Березина Николь Владиславовна     | выше 75к       | есть   |
-- | Волкова Ева Егоровна              | выше 75к       | есть   |
-- | Воробьева Ева Фёдоровна           | выше 75к       | есть   |
-- | Дроздов Степан Максимович         | выше 75к       | есть   |
-- | Зайцева Таисия Марковна           | выше 75к       | есть   |
-- | Злобин Илья Алексеевич            | выше 75к       | есть   |
-- | Иванов Савва Дмитриевич           | выше 75к       | есть   |
-- | Иванова Мария Романовна           | выше 75к       | есть   |
-- | Князев Руслан Максимович          | выше 75к       | есть   |
-- | Лебедев Платон Михайлович         | выше 75к       | есть   |
-- | Леонов Егор Матвеевич             | выше 75к       | есть   |
-- | Миронов Никита Матвеевич          | выше 75к       | есть   |
-- | Никулин Ярослав Михайлович        | выше 75к       | есть   |
-- | Савин Родион Михайлович           | выше 75к       | есть   |
-- | Скворцова Елизавета Мирославовна  | выше 75к       | есть   |
-- | Соколова София Михайловна         | выше 75к       | есть   |
-- | Суслова Ольга Матвеевна           | выше 75к       | есть   |
-- | Суханов Павел Даниилович          | выше 75к       | есть   |
-- | Фомина Ксения Васильевна          | выше 75к       | есть   |
-- +-----------------------------------+----------------+--------+
-- 70 rows in set (0.0009 sec)


select
  count(*) as `люди`,
  if(salary > 75000, 'выше 75к', 'ниже 75к') as `уровень оклада`,
  if(premium > 0, 'есть', 'нет') as `премия`
from doctors
group by `уровень оклада`, `премия`
order by `уровень оклада` desc, `премия` desc;

-- +------+----------------+--------+
-- | люди | уровень оклада | премия |
-- +------+----------------+--------+
-- |   16 | ниже 75к       | нет    |
-- |   21 | ниже 75к       | есть   |
-- |   14 | выше 75к       | нет    |
-- |   19 | выше 75к       | есть   |
-- +------+----------------+--------+
-- 4 rows in set (0.0008 sec)


select
  count(*) as `люди`,
  if(salary > 75000, 'выше 75к', 'ниже 75к') as `уровень оклада`,
  if(premium > 0, 'есть', 'нет') as `премия`
from doctors
group by `уровень оклада`, `премия` with rollup
order by `уровень оклада` desc, `премия` desc;

-- +------+----------------+--------+
-- | люди | уровень оклада | премия |
-- +------+----------------+--------+
-- |   16 | ниже 75к       | нет    |
-- |   21 | ниже 75к       | есть   |
-- |   37 | ниже 75к       | NULL   |
-- |   14 | выше 75к       | нет    |
-- |   19 | выше 75к       | есть   |
-- |   33 | выше 75к       | NULL   |
-- |   70 | NULL           | NULL   |
-- +------+----------------+--------+
-- 7 rows in set (0.0038 sec)


select
  count(*) as `люди`,
  if(salary > 75000, 'выше 75к', 'ниже 75к') as `уровень оклада`,
  if(premium > 0, 'есть', 'нет') as `премия`,
  grouping(if(premium > 0, 'есть', 'нет')) as 'все премии',
  grouping(if(salary > 75000, 'выше 75к', 'ниже 75к')) as 'все оклады'
from doctors
group by `уровень оклада`, `премия` with rollup;

-- +------+----------------+--------+------------+------------+
-- | люди | уровень оклада | премия | все премии | все оклады |
-- +------+----------------+--------+------------+------------+
-- |   19 | выше 75к       | есть   |          0 |          0 |
-- |   14 | выше 75к       | нет    |          0 |          0 |
-- |   33 | выше 75к       | NULL   |          1 |          0 |
-- |   21 | ниже 75к       | есть   |          0 |          0 |
-- |   16 | ниже 75к       | нет    |          0 |          0 |
-- |   37 | ниже 75к       | NULL   |          1 |          0 |
-- |   70 | NULL           | NULL   |          1 |          1 |
-- +------+----------------+--------+------------+------------+
-- 7 rows in set (0.0008 sec)

