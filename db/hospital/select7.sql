select count(*) 
  from sponsors;

-- +----------+
-- | count(*) |
-- +----------+
-- |       13 |
-- +----------+
-- 1 row in set (0.0013 sec)


select sponsor, count(*) 
  from sponsors;

-- ERROR: 1140 (42000): In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'hospital.sponsors.sponsor'; this is incompatible with sql_mode=only_full_group_by


select 
  1 + 1 as col1, 
  count(*) as `all rows`
from sponsors;

-- +------+----------+
-- | col1 | all rows |
-- +------+----------+
-- |    2 |       13 |
-- +------+----------+
-- 1 row in set (0.0012 sec)



