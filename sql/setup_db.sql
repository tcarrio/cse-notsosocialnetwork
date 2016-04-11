drop table if exists users;
drop table if exists profiles;

create table users (
    user_id int not null auto_increment,
    user_first_name varchar(255) not null,
    user_last_name varchar(255) not null,
    user_email varchar(255) not null,
    user_password char(64) not null,
    user_dob timestamp not null,
    user_gender boolean not null,
    primary key (user_id)
);

create table profiles (
    profile_id int not null auto_increment,
    profile_uri varchar(255) not null,
    profile_about varchar(1023) not null,
    user_id int,
    primary key (profile_id),
    foreign key (user_id) references users(user_id)
)