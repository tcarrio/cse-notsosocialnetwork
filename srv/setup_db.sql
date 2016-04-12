drop table if exists messages;
drop table if exists posts;
drop table if exists profiles;
drop table if exists accounts;

create table accounts (
    account_email varchar(255) not null,
    account_first_name varchar(255) not null,
    account_last_name varchar(255) not null,
    account_password char(64) not null,
    account_dob timestamp not null,
    account_gender boolean not null,
    primary key (account_email)
);

create table profiles (
    profile_id int not null auto_increment,
    profile_uri varchar(255) not null,
    profile_about varchar(1023) not null,
    account_email varchar(255),
    primary key (profile_id),
    foreign key (account_email) references accounts(account_email)
);

create table posts (
    post_id int not null auto_increment,
    post_uri varchar(255) not null,
    account_email varchar(255) not null,
    receiver_email varchar(255),
    post_date timestamp not null,
    post_content varchar(4096) not null,
    primary key (post_id),
    foreign key (account_email) references accounts(account_email),
    foreign key (receiver_email) references accounts(account_email)
);

create table messages (
    message_id int not null auto_increment,
    message_uri varchar(255) not null,
    account_email varchar(255) not null,
    receiver_email varchar(255) not null,
    message_date timestamp not null,
    message_title varchar(255) not null,
    message_content varchar(4096) not null,
    primary key (message_id),
    foreign key (account_email) references accounts(account_email),
    foreign key (receiver_email) references accounts(account_email)
);