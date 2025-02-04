CREATE TABLE users (
    user_id int NOT NULL AUTO_INCREMENT, 
    username varchar(255) UNIQUE,
    user_email varchar(255),
    user_password varchar(255),
    user_first_name varchar(255),
    user_last_name varchar(255),
    PRIMARY KEY (user_id)
)