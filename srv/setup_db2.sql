drop table if exists messages;
drop table if exists posts;
drop table if exists accounts;

create table accounts (
    uri int not null auto_increment,
    email varchar(255) not null unique,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    password char(64) not null,
    dob timestamp not null,
    gender boolean not null,
    about varchar(1023),
    primary key (uri)
);

create table posts (
    post_id int not null auto_increment,
    post_uri varchar(255) not null,
    sender_email varchar(255) not null,
    receiver_email varchar(255),
    post_date timestamp not null,
    post_content varchar(4096) not null,
    primary key (post_id),
    foreign key (sender_email) references accounts(email),
    foreign key (receiver_email) references accounts(email)
);

create table messages (
    message_id int not null auto_increment,
    message_uri varchar(255) not null,
    sender_email varchar(255) not null,
    receiver_email varchar(255) not null,
    message_date timestamp not null,
    message_title varchar(255) not null,
    message_content varchar(4096) not null,
    primary key (message_id),
    foreign key (sender_email) references accounts(email),
    foreign key (receiver_email) references accounts(email)
);