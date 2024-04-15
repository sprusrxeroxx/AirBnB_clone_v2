-- A script to a new database hbnb_dev_db which will host the 
-- Airbnb data

CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

USE hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' 
    IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost'





