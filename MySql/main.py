import mysql.connector
from Query_Writer_Class import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE testdb")

# my_cursor.execute("show databases")

# my_cursor.execute(
# """CREATE TABLE users (
# name varchar(40),
# email varchar(40),
# age integer(3),
# user_id integer AUTO_INCREMENT,
# PRIMARY KEY (user_id)
# )"""
# )

# insert_quarry = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record_1 = "Micu", "micking3@op.pl", 33
# my_cursor.execute(insert_quarry, record_1)
# record_list = [
#     ("Aykari", "aya@vp.com", 33),
#     ("Turka", "tura@jj.tr", 12),
#     ("Maria", "Mari@gmail.pl",62)
# ]


# my_cursor.executemany(insert_quarry, record_list)
# mydb.commit()
# my_cursor.execute("SELECT * From users")
# result = my_cursor.fetchall()
# for row in result:
#     print(f"{row[0]}\t{row[1]}\t{row[2]}\t {row[3]}")

# update_quarry = "UPDATE users SET email = 'tura@jj.tr' WHERE name = 'Turka' "
# my_cursor.execute(update_quarry)
# mydb.commit()

# my_cursor.execute("SELECT * FROM users ORDER BY name DESC LIMIT 3 OFFSET 1")
# result = my_cursor.fetchall()
# for row in result:
#     print(f"{row[0]}\t{row[1]}\t{row[2]}\t {row[3]}")

query_1 = QueryWriter()
my_cursor.execute(str(query_1.select().from_st("users").where("user_id = 3")))
result = my_cursor.fetchall()
for row in result:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t {row[3]}")
