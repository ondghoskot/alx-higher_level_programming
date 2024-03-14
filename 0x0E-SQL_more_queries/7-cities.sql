-- script that creates a database and table
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states`(`id` INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
`state_id` INT NOT NULL, FOREIGN KEY (`state_id`) REFERENCES `states`(`ìd`),
`name` VARCHAR(256) NOT NULL);