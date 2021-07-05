-- Andrew Schaefer
-- 6/26/21
-- CSD310
-- Module 8.2


-- Drop test user if exists
DROP USER IF EXISTS 'pysports_user'@'localhost';

-- Create pysports user and grant them all privileges to pysports database
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'weare138';

-- Grant all privileges to the pysports database to user pysports_user on localhost
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';

-- Drop tables if they are present
DROP TABLE IF EXISTS player;

-- Create team table
CREATE TABLE team (
    team_id     INT          NOT NULL    AUTO_INCREMENT,
    team_name   VARCHAR(75)  NOT NULL,
    mascot      VARCHAR(75)  NOT NULL,
    PRIMARY KEY(team_id) 
);

-- Create player table
CREATE TABLE player (
    player_id   INT          NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75)  NOT NULL,
    last_name   VARCHAR(75)  NOT NULL,
    team_id     INT          NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id) REFERENCES team(team_id) 
);

-- Insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Sampson Scorpions','Scorpion');

INSERT INTO team(team_name, mascot)
    VALUES('Payne Polar Bears','Polar Bear');

-- Insert player records
INSERT INTO player(first_name, last_name, team_id)
    VALUES('Jack', 'Sparrow', 1);

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Ray', 'Kurzweil', 2);

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Christopher', 'Colburn', 1);

SELECT team_id FROM team WHERE team_name = 'Payne Polar Bears';




