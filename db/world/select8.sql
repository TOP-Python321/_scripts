select name, indepyear from country limit 5;

-- +-------------+-----------+
-- | name        | indepyear |
-- +-------------+-----------+
-- | Aruba       |      NULL |
-- | Afghanistan |      1919 |
-- | Angola      |      1975 |
-- | Anguilla    |      NULL |
-- | Albania     |      1912 |
-- +-------------+-----------+
-- 5 rows in set (0.0005 sec)


select count(*) from country;

-- +----------+
-- | count(*) |
-- +----------+
-- |      239 |
-- +----------+
-- 1 row in set (0.0016 sec)
 
 
select count(indepyear) from country;

-- +------------------+
-- | count(indepyear) |
-- +------------------+
-- |              192 |
-- +------------------+
-- 1 row in set (0.0006 sec)


select count(*) 
  from country 
 limit 5;

-- +----------+
-- | count(*) |
-- +----------+
-- |      239 |
-- +----------+
-- 1 row in set (0.0014 sec)
 

select count(indepyear) 
  from country 
 limit 5;

-- +------------------+
-- | count(indepyear) |
-- +------------------+
-- |              192 |
-- +------------------+
-- 1 row in set (0.0005 sec)


select count(*)
  from (select * from country limit 5) as subq;

-- +----------+
-- | count(*) |
-- +----------+
-- |        5 |
-- +----------+
-- 1 row in set (0.0008 sec)
 

select count(subq.indepyear) 
  from (select indepyear from country limit 5) as subq;

-- +-----------------------+
-- | count(subq.indepyear) |
-- +-----------------------+
-- |                     3 |
-- +-----------------------+
-- 1 row in set (0.0006 sec)

