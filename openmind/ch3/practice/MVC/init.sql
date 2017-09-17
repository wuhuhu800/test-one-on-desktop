drop table if exists users;
create table users (
  id INTEGER PRIMARY key autoincrement,
  name text not null,
  password text not NULL
);
insert into users (name,password) values('visit','111');
insert into users (name,password) values('admin','123');
