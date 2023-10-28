select 
    curdate(), 
    concat_ws(' — ', code, name) 
from country 
limit 10;

-- +------------+------------------------------+
-- | curdate()  | concat_ws(' — ', code, name) |
-- +------------+------------------------------+
-- | 2023-10-22 | ABW — Aruba                  |
-- | 2023-10-22 | AFG — Afghanistan            |
-- | 2023-10-22 | AGO — Angola                 |
-- | 2023-10-22 | AIA — Anguilla               |
-- | 2023-10-22 | ALB — Albania                |
-- | 2023-10-22 | AND — Andorra                |
-- | 2023-10-22 | ANT — Netherlands Antilles   |
-- | 2023-10-22 | ARE — United Arab Emirates   |
-- | 2023-10-22 | ARG — Argentina              |
-- | 2023-10-22 | ARM — Armenia                |
-- +------------+------------------------------+
-- 10 rows in set (0.0007 sec)


select 
    concat_ws(' — ', code, name) as 'CODE — Country' 
from country 
limit 5, 10;

-- +-----------------------------------+
-- | CODE — Country                    |
-- +-----------------------------------+
-- | AND — Andorra                     |
-- | ANT — Netherlands Antilles        |
-- | ARE — United Arab Emirates        |
-- | ARG — Argentina                   |
-- | ARM — Armenia                     |
-- | ASM — American Samoa              |
-- | ATA — Antarctica                  |
-- | ATF — French Southern territories |
-- | ATG — Antigua and Barbuda         |
-- | AUS — Australia                   |
-- +-----------------------------------+
-- 10 rows in set (0.0017 sec)

