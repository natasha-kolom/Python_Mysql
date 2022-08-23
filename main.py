import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")

    try:
        #create table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE users (id int AUTO_INCREMENT, " \
        #                          "name varchar(32), password varchar(32)," \
        #                          " email varchar(32), PRIMARY KEY(id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")

        # #insert data
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO users (name, password, email) VALUES('Anna', 'qwerty', 'anna@g.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        #update data
        with connection.cursor() as cursor:
            update_query = "UPDATE users SET password = 'xxxXXX' WHERE id = 1"
            cursor.execute(update_query)
            connection.commit()

        #delete data
        with connection.cursor() as cursor:
            delete_query = "DELETE FROM users WHERE id = 1;"
            cursor.execute(delete_query)
            connection.commit()



        #select all data from table
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM users"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        #drop table
        with connection.cursor() as cursor:
            drop_table_query = "DROP TABLE users"
            cursor.execute(drop_table_query)




    finally:
        connection.close()
except Exception as ex:
    print("Connection refused...")
    print(ex)