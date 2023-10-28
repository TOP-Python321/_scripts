select name 
from country 
where population > 100000000;

-- +--------------------+
-- | name               |
-- +--------------------+
-- | Bangladesh         |
-- | Brazil             |
-- | China              |
-- | Indonesia          |
-- | India              |
-- | Japan              |
-- | Nigeria            |
-- | Pakistan           |
-- | Russian Federation |
-- | United States      |
-- +--------------------+
-- 10 rows in set (0.0006 sec)


select code from country where name = 'Russian Federation';

-- +------+
-- | code |
-- +------+
-- | RUS  |
-- +------+
-- 1 row in set (0.0008 sec)


select name, district
  from city
 where countrycode = 'RUS' 
   and population > 1000000;

-- +----------------+----------------+
-- | name           | district       |
-- +----------------+----------------+
-- | Moscow         | Moscow (City)  |
-- | St Petersburg  | Pietari        |
-- | Novosibirsk    | Novosibirsk    |
-- | Nizni Novgorod | Nizni Novgorod |
-- | Jekaterinburg  | Sverdlovsk     |
-- | Samara         | Samara         |
-- | Omsk           | Omsk           |
-- | Kazan          | Tatarstan      |
-- | Ufa            | Baškortostan   |
-- | Tšeljabinsk    | Tšeljabinsk    |
-- | Rostov-na-Donu | Rostov-na-Donu |
-- | Perm           | Perm           |
-- +----------------+----------------+
-- 12 rows in set (0.0010 sec)


select countrycode, name
  from city
 where name like '%burg';

-- +-------------+------------------+
-- | countrycode | name             |
-- +-------------+------------------+
-- | NLD         | Tilburg          |
-- | ZAF         | Johannesburg     |
-- | ZAF         | Pietermaritzburg |
-- | ZAF         | Randburg         |
-- | ZAF         | Boksburg         |
-- | ZAF         | Rustenburg       |
-- | AUT         | Salzburg         |
-- | DEU         | Hamburg          |
-- | DEU         | Duisburg         |
-- | DEU         | Augsburg         |
-- | DEU         | Magdeburg        |
-- | DEU         | Oldenburg        |
-- | DEU         | Würzburg         |
-- | DEU         | Regensburg       |
-- | DEU         | Wolfsburg        |
-- | RUS         | St Petersburg    |
-- | RUS         | Jekaterinburg    |
-- | RUS         | Orenburg         |
-- | USA         | Saint Petersburg |
-- +-------------+------------------+
-- 19 rows in set (0.0067 sec)


select countrycode, language, percentage
  from countrylanguage
 where language = 'english'
   and percentage between 5 and 20;

-- +-------------+----------+------------+
-- | countrycode | language | percentage |
-- +-------------+----------+------------+
-- | ABW         | English  |        9.5 |
-- | ANT         | English  |        7.8 |
-- | LCA         | English  |       20.0 |
-- | MCO         | English  |        6.5 |
-- | NRU         | English  |        7.5 |
-- | ZAF         | English  |        8.5 |
-- +-------------+----------+------------+
-- 6 rows in set (0.0010 sec)

