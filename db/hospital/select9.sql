select count(first_name) 
  from doctors;

-- +-------------------+
-- | count(first_name) |
-- +-------------------+
-- |                70 |
-- +-------------------+
-- 1 row in set (0.0012 sec)


select count(distinct first_name) 
  from doctors;

-- +----------------------------+
-- | count(distinct first_name) |
-- +----------------------------+
-- |                         52 |
-- +----------------------------+
-- 1 row in set (0.0006 sec)


select count(distinct first_name, patr_name) 
  from doctors;

-- +---------------------------------------+
-- | count(distinct first_name, patr_name) |
-- +---------------------------------------+
-- |                                    69 |
-- +---------------------------------------+
-- 1 row in set (0.0008 sec)


select count(distinct last_name, first_name, patr_name) 
  from doctors;

-- +--------------------------------------------------+
-- | count(distinct last_name, first_name, patr_name) |
-- +--------------------------------------------------+
-- |                                               70 |
-- +--------------------------------------------------+


