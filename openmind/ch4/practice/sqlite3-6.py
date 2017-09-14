#碰到问题尚未解决：AttributeError: 'sqlite3.Connection' object has no attribute 'enable_load_extension'
#https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.enable_load_extension
#https://gxnotes.com/article/165331.html(set.cfg文件有一行被注释掉了，“然后编辑setup.cfg文件以注释掉SQLITE_OMIT_LOAD_EXTENSION指令：

import sqlite3
con = sqlite3.connect(":memory:")
con.enable_load_extension(True)
con.lord_extension("./ft3.so")
con.execute("create vitual table ricipe using fts(name,ingredients) ")
con.executescript("""
    insert into ricipe(name,ingredients) values('broccoli stew', 'broccoli peppers cheese tomatoes');
    insert into ricipe(name,ingredients) values('pumpkin stew','pumpkin onions garlic celery');
    insert into ricipe(name,ingredients) values('broccoli pie','broccoli cheese onions flour');
    insert into ricipe(name,ingredients) values ('pumpkin pie', 'pumpkin sugar flour butter');
    """)
for row in con.execute("select rowid ,name, ingredients from ricipe where name match 'pie' "):
    print(row)
