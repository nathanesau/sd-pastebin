-- example insert queries
insert into pastes(shortlink, expiration_length_in_minutes, created_at, paste_path) values('foobar', 60, now(), '/foobar.txt');
insert into pastes(shortlink, expiration_length_in_minutes, created_at, paste_path) values('short', 20, now(), '/path.txt');