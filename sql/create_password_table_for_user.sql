CREATE TABLE --their username (
    password_id int NOT NULL AUTO_INCREMENT,
    website_name varchar(255),
    website_url varchar(255),
    password_username varchar(255),
    password_password varchar(255),
    length_score int,
    number_score int,
    case_score int,
    symbol_score int,
    overall_score int,
    improved_password varchar(255),
    new_overall_score int,
    security_fields varchar(255),
    PRIMARY KEY (password_id)
)