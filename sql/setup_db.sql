drop table if exists users;

create table users (
    user_id int not null auto_increment,
    user_first_name varchar(255) not null,
    user_last_name varchar(255) not null,
    user_email varchar(255) not null,
    user_password varchar(255) not null,
    user_dob timestamp not null,
    user_gender boolean not null,
    primary key (user_id)
);