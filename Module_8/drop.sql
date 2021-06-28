
-- Drop test user if exists
DROP USER IF EXISTS 'pysports_user'@'localhost';

-- Create pysports user and grant them all privileges to pysports database
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'weare138';

-- Grant all privileges to the pysports database to user pysports_user on localhost
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';

-- Drop tables if they are present
DROP TABLE player;
DROP TABLE team;
