import sqlite3

# import click
# from flask import current_app, g

# print("Initializing db.py...")
# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(
#             current_app.config['DATABASE'],
#             detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = sqlite3.Row

#     return g.db


# # def close_db(e=None):
# #     db = g.pop('db', None)

# #     if db is not None:
# #         db.close()

# def init_db():
#     db = get_db()

#     with current_app.open_resource('schema.sql') as f:
#         db.executescript(f.read().decode('utf8'))



# init_db()
# click.echo('Initialized the database.')

# def init_app(app):
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command)


connection = sqlite3.connect('TLM2008_Project/database.db')


# with open('TLM2008_Project\schema.sql') as f:
#     connection.executescript(f.read())

# cur = connection.cursor()

# connection.commit()
# connection.close()


# connection.execute("CREATE TABLE auction_bids (item_id INTEGER,auction_id INTEGER, user_id INTEGER, bid_amount INTEGER,transaction_date DATETIME, PRIMARY KEY (auction_id, user_id))")
# connection.commit()

# connection.execute("Delete from auction_bids")
# connection.commit()

# connection.execute("CREATE TABLE auction_item(item_id INTEGER, item_name TEXT, item_description TEXT, item_starting_price INTEGER, item_current_price INTEGER, item_end_date DATETIME, item_image_url TEXT, PRIMARY KEY (item_id))")
# connection.commit()

# connection.execute("Insert into auction_item(item_id, item_name, item_description, item_starting_price, item_current_price, item_end_date, item_image_url) values (2,'Dimoo','This is item 1',100,100,'2020-12-31 23:59:59','img/POPtrade/WHAT_I_USED/Dimoo/1.webp')")
# connection.commit()

# connection.execute("drop table auction_bids")
# connection.commit()

# connection.execute("Insert into auction_item(item_id, item_name, item_description, item_starting_price, item_current_price, item_end_date, item_image_url) values (6,'han','han series',2199,10000,'2023-12-31 23:59:59','img/POPtrade/WHAT_I_USED/han/1.webp')")

# connection.execute("ALTER TABLE listed_item add series varchar(255);")

# connection.execute("create table listed_item_sub(parent_item_id,item_id item_name, item_description, item_price, item_image_url, PRIMARY KEY (item_id))")

connection.execute("update listed_item set item_image_url = 'img/POPtrade/WHAT_I_USED/PuckyxSanrio/1.webp' where item_id == 7")

# connection.execute("alter table user_info add contactNo TEXT")

# connection.execute("create table user_info(user_id INTEGER, username TEXT,userRating FLOAT,userTotalListing INTEGER, PRIMARY KEY (user_id))")


# connection.execute("delete from auction_item where item_id = 4")

#connection.execute("insert into user_info(user_id,username,userRating,userTotalListing) values (2,'user2',3.2,2)")

#connection.execute("insert into listed_item(item_id,item_name,item_description,item_starting_price,item_image_url,item_catergory,series,user_id) values (11,'mickey','mickey series 7/13',78,'img/POPtrade/WHAT_I_USED/mickey/7.webp','market','NO','8')")
#connection.execute("delete from listed_item where item_id = 7")

connection.commit()