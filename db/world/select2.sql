select code, name from country;

-- +------+----------------------------------------------+
-- | code | name                                         |
-- +------+----------------------------------------------+
-- | ABW  | Aruba                                        |
-- | AFG  | Afghanistan                                  |
-- | AGO  | Angola                                       |
-- | AIA  | Anguilla                                     |
-- | ALB  | Albania                                      |
-- .......................................................
-- +------+----------------------------------------------+
-- 239 rows in set (0.1812 sec)


select 1, code, name from country;

-- +---+------+----------------------------------------------+
-- | 1 | code | name                                         |
-- +---+------+----------------------------------------------+
-- | 1 | ABW  | Aruba                                        |
-- | 1 | AFG  | Afghanistan                                  |
-- | 1 | AGO  | Angola                                       |
-- | 1 | AIA  | Anguilla                                     |
-- | 1 | ALB  | Albania                                      |
-- ...........................................................
-- +------+--------------------------------------------------+
-- 239 rows in set (0.1812 sec)


select curdate(), concat_ws(' — ', code, name) from country;

-- +------------+----------------------------------------------------+
-- | curdate()  | concat_ws(' — ', code, name)                       |
-- +------------+----------------------------------------------------+
-- | 2023-10-22 | ABW — Aruba                                        |
-- | 2023-10-22 | AFG — Afghanistan                                  |
-- | 2023-10-22 | AGO — Angola                                       |
-- | 2023-10-22 | AIA — Anguilla                                     |
-- | 2023-10-22 | ALB — Albania                                      |
-- ...................................................................
-- +------+----------------------------------------------------------+
-- 239 rows in set (0.1812 sec)

