select *
from t1
join t2
order by id1, id2;

-- +-----+-----------+-----+-----------+-------+
-- | id1 | name1     | id2 | name2     | t1_id |
-- +-----+-----------+-----+-----------+-------+
-- |   1 | таблица 1 |   1 | таблица 2 |     1 |
-- |   1 | таблица 1 |   2 | таблица 2 |     3 |
-- |   1 | таблица 1 |   3 | таблица 2 |     1 |
-- |   1 | таблица 1 |   4 | таблица 2 |     2 |
-- |   1 | таблица 1 |   5 | таблица 2 |     2 |
-- |   1 | таблица 1 |   6 | таблица 2 |     1 |
-- |   2 | таблица 1 |   1 | таблица 2 |     1 |
-- |   2 | таблица 1 |   2 | таблица 2 |     3 |
-- |   2 | таблица 1 |   3 | таблица 2 |     1 |
-- |   2 | таблица 1 |   4 | таблица 2 |     2 |
-- |   2 | таблица 1 |   5 | таблица 2 |     2 |
-- |   2 | таблица 1 |   6 | таблица 2 |     1 |
-- |   3 | таблица 1 |   1 | таблица 2 |     1 |
-- |   3 | таблица 1 |   2 | таблица 2 |     3 |
-- |   3 | таблица 1 |   3 | таблица 2 |     1 |
-- |   3 | таблица 1 |   4 | таблица 2 |     2 |
-- |   3 | таблица 1 |   5 | таблица 2 |     2 |
-- |   3 | таблица 1 |   6 | таблица 2 |     1 |
-- +-----+-----------+-----+-----------+-------+
-- 18 rows in set (0.0009 sec)


select *
from t1
join t2 on t1.id1 = t2.t1_id;

-- +-----+-----------+-----+-----------+-------+
-- | id1 | name1     | id2 | name2     | t1_id |
-- +-----+-----------+-----+-----------+-------+
-- |   1 | таблица 1 |   1 | таблица 2 |     1 |
-- |   3 | таблица 1 |   2 | таблица 2 |     3 |
-- |   1 | таблица 1 |   3 | таблица 2 |     1 |
-- |   2 | таблица 1 |   4 | таблица 2 |     2 |
-- |   2 | таблица 1 |   5 | таблица 2 |     2 |
-- |   1 | таблица 1 |   6 | таблица 2 |     1 |
-- +-----+-----------+-----+-----------+-------+
-- 6 rows in set (0.0007 sec)



