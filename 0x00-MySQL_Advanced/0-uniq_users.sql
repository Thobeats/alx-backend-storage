--Write a SQL script that creates a user table
---id, integer, never null, auto increment and primary key
---email, string (255 characters), never null and unique
---name, string (255 characters)
--If the table already exists, your script should not fail
--Your script can be executed on any database

use holberton;

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);