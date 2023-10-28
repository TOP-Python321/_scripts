select *
  from vacations
 where datediff(end_date, start_date) <= 40;

-- +-----+------------+------------+------------+
-- | id  | start_date | end_date   | doctors_id |
-- +-----+------------+------------+------------+
-- |  66 | 2009-02-20 | 2009-03-29 |         24 |
-- | 147 | 2013-06-07 | 2013-06-22 |         35 |
-- | 201 | 2008-07-28 | 2008-08-23 |         48 |
-- | 279 | 2016-12-14 | 2017-01-16 |         21 |
-- | 343 | 2020-08-25 | 2020-09-12 |         22 |
-- | 413 | 2005-07-19 | 2005-07-26 |          8 |
-- | 581 | 2007-12-25 | 2007-12-27 |         14 |
-- +-----+------------+------------+------------+
-- 7 rows in set (0.0012 sec)


delete from vacations limit 684;

-- Query OK, 684 rows affected (0.0258 sec)


update vacations
   set end_date = adddate(start_date, floor(5 + rand()*39))
 where datediff(end_date, start_date) > 40;

-- Query OK, 300 rows affected (0.0191 sec)
-- Rows matched: 300  Changed: 300  Warnings: 0

