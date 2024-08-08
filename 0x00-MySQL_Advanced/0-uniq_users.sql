--Write a SQL script that creates a user table
---id, integer, never null, auto increment and primary key
---email, string (255 characters), never null and unique
---name, string (255 characters)
--If the table already exists, your script should not fail
--Your script can be executed on any database

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255)
)