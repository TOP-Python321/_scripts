select 
    code, 
    name, 
    localname 
from country 
limit 15;

-- +------+-----------------------------+------------------------------------+
-- | code | name                        | localname                          |
-- +------+-----------------------------+------------------------------------+
-- | ABW  | Aruba                       | Aruba                              |
-- | AFG  | Afghanistan                 | Afganistan/Afqanestan              |
-- | AGO  | Angola                      | Angola                             |
-- | AIA  | Anguilla                    | Anguilla                           |
-- | ALB  | Albania                     | Shqipëria                          |
-- | AND  | Andorra                     | Andorra                            |
-- | ANT  | Netherlands Antilles        | Nederlandse Antillen               |
-- | ARE  | United Arab Emirates        | Al-Imarat al-´Arabiya al-Muttahida |
-- | ARG  | Argentina                   | Argentina                          |
-- | ARM  | Armenia                     | Hajastan                           |
-- | ASM  | American Samoa              | Amerika Samoa                      |
-- | ATA  | Antarctica                  | –                                  |
-- | ATF  | French Southern territories | Terres australes françaises        |
-- | ATG  | Antigua and Barbuda         | Antigua and Barbuda                |
-- | AUS  | Australia                   | Australia                          |
-- +------+-----------------------------+------------------------------------+
-- 15 rows in set (0.0008 sec)


  select code, 
         name, 
         localname 
    from country 
order by name 
   limit 15;

-- +------+---------------------+-----------------------+
-- | code | name                | localname             |
-- +------+---------------------+-----------------------+
-- | AFG  | Afghanistan         | Afganistan/Afqanestan |
-- | ALB  | Albania             | Shqipëria             |
-- | DZA  | Algeria             | Al-Jaza’ir/Algérie    |
-- | ASM  | American Samoa      | Amerika Samoa         |
-- | AND  | Andorra             | Andorra               |
-- | AGO  | Angola              | Angola                |
-- | AIA  | Anguilla            | Anguilla              |
-- | ATA  | Antarctica          | –                     |
-- | ATG  | Antigua and Barbuda | Antigua and Barbuda   |
-- | ARG  | Argentina           | Argentina             |
-- | ARM  | Armenia             | Hajastan              |
-- | ABW  | Aruba               | Aruba                 |
-- | AUS  | Australia           | Australia             |
-- | AUT  | Austria             | Österreich            |
-- | AZE  | Azerbaijan          | Azärbaycan            |
-- +------+---------------------+-----------------------+
-- 15 rows in set (0.0050 sec)


select 
  countrycode,
  name,
  population
from city 
order by countrycode, population desc 
limit 15;

-- +-------------+------------------+------------+
-- | countrycode | name             | population |
-- +-------------+------------------+------------+
-- | ABW         | Oranjestad       |      29034 |
-- | AFG         | Kabul            |    1780000 |
-- | AFG         | Qandahar         |     237500 |
-- | AFG         | Herat            |     186800 |
-- | AFG         | Mazar-e-Sharif   |     127800 |
-- | AGO         | Luanda           |    2022000 |
-- | AGO         | Huambo           |     163100 |
-- | AGO         | Lobito           |     130000 |
-- | AGO         | Benguela         |     128300 |
-- | AGO         | Namibe           |     118200 |
-- | AIA         | South Hill       |        961 |
-- | AIA         | The Valley       |        595 |
-- | ALB         | Tirana           |     270000 |
-- | AND         | Andorra la Vella |      21189 |
-- | ANT         | Willemstad       |       2345 |
-- +-------------+------------------+------------+
-- 15 rows in set (0.0040 sec)


select 
    countrycode, 
    name, 
    population 
from city 
order by countrycode desc, population desc 
limit 15;

-- +-------------+--------------+------------+
-- | countrycode | name         | population |
-- +-------------+--------------+------------+
-- | ZWE         | Harare       |    1410000 |
-- | ZWE         | Bulawayo     |     621742 |
-- | ZWE         | Chitungwiza  |     274912 |
-- | ZWE         | Mount Darwin |     164362 |
-- | ZWE         | Mutare       |     131367 |
-- | ZWE         | Gweru        |     128037 |
-- | ZMB         | Lusaka       |    1317000 |
-- | ZMB         | Ndola        |     329200 |
-- | ZMB         | Kitwe        |     288600 |
-- | ZMB         | Kabwe        |     154300 |
-- | ZMB         | Chingola     |     142400 |
-- | ZMB         | Mufulira     |     123900 |
-- | ZMB         | Luanshya     |     118100 |
-- | ZAF         | Cape Town    |    2352121 |
-- | ZAF         | Soweto       |     904165 |
-- +-------------+--------------+------------+
-- 15 rows in set (0.0035 sec)


select 
    name, 
    population, 
    gnp, 
    gnp / population as `gdp by ppp`
from country 
order by gnp / population desc;

-- +----------------------------------------------+------------+------------+------------+
-- | name                                         | population | gnp        | gdp by ppp |
-- +----------------------------------------------+------------+------------+------------+
-- | Luxembourg                                   |     435700 |   16321.00 |   0.037459 |
-- | Switzerland                                  |    7160400 |  264478.00 |   0.036936 |
-- | Bermuda                                      |      65000 |    2328.00 |   0.035815 |
-- | Brunei                                       |     328000 |   11705.00 |   0.035686 |
-- | Liechtenstein                                |      32300 |    1119.00 |   0.034644 |
-- | Cayman Islands                               |      38000 |    1263.00 |   0.033237 |
-- | Denmark                                      |    5330000 |  174099.00 |   0.032664 |
-- | Norway                                       |    4478500 |  145895.00 |   0.032577 |
-- | United States                                |  278357000 | 8510700.00 |   0.030575 |
-- | Japan                                        |  126714000 | 3787042.00 |   0.029887 |
-- | Iceland                                      |     279000 |    8255.00 |   0.029588 |
-- | Virgin Islands, British                      |      21000 |     612.00 |   0.029143 |
-- | Austria                                      |    8091800 |  211860.00 |   0.026182 |
-- | Germany                                      |   82164700 | 2133367.00 |   0.025965 |
-- | Sweden                                       |    8861400 |  226492.00 |   0.025559 |
-- .......................................................................................
-- +----------------------------------------------+------------+------------+------------+
-- 239 rows in set, 14 warnings (0.0012 sec)


select 
    name, 
    population, 
    gnp, 
    gnp / population as `gdp by ppp`
from country 
order by `gdp by ppp` desc;

-- +----------------------------------------------+------------+------------+------------+
-- | name                                         | population | gnp        | gdp by ppp |
-- +----------------------------------------------+------------+------------+------------+
-- | Luxembourg                                   |     435700 |   16321.00 |   0.037459 |
-- | Switzerland                                  |    7160400 |  264478.00 |   0.036936 |
-- | Bermuda                                      |      65000 |    2328.00 |   0.035815 |
-- | Brunei                                       |     328000 |   11705.00 |   0.035686 |
-- | Liechtenstein                                |      32300 |    1119.00 |   0.034644 |
-- | Cayman Islands                               |      38000 |    1263.00 |   0.033237 |
-- | Denmark                                      |    5330000 |  174099.00 |   0.032664 |
-- | Norway                                       |    4478500 |  145895.00 |   0.032577 |
-- | United States                                |  278357000 | 8510700.00 |   0.030575 |
-- | Japan                                        |  126714000 | 3787042.00 |   0.029887 |
-- | Iceland                                      |     279000 |    8255.00 |   0.029588 |
-- | Virgin Islands, British                      |      21000 |     612.00 |   0.029143 |
-- | Austria                                      |    8091800 |  211860.00 |   0.026182 |
-- | Germany                                      |   82164700 | 2133367.00 |   0.025965 |
-- | Sweden                                       |    8861400 |  226492.00 |   0.025559 |
-- .......................................................................................
-- +----------------------------------------------+------------+------------+------------+
-- 239 rows in set, 14 warnings (0.0012 sec)

