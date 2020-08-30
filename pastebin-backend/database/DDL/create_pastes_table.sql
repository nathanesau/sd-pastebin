create table pastes
(
shortlink char(7) not null,
expiration_length_in_minutes int not null,
created_at date not null,
paste_path varchar(255) not null,
primary key(shortlink)
);
