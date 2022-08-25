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
        with connection.cursor() as cursor:
             create_table_query = "CREATE TABLE IF NOT EXISTS users (id int AUTO_INCREMENT, " \
                                  "name varchar(32), password varchar(32)," \
                                  " email varchar(32), PRIMARY KEY(id));"
             cursor.execute(create_table_query)
             print("Table created successfully")

        with connection.cursor() as cursor:
             create_table_query = "CREATE TABLE IF NOT EXISTS passports (id int AUTO_INCREMENT, " \
                                  "passport_number int NOT NULL, city_of_registration varchar(32)," \
                                  "fk_passport_users int, PRIMARY KEY(id)," \
                                  "FOREIGN KEY (fk_passport_users) REFERENCES users(id));"
             cursor.execute(create_table_query)
             print("Table created successfully")

        with connection.cursor() as cursor:
            query = "CREATE TABLE posts (" \
                    "id int  PRIMARY KEY," \
                    "post_title varchar(150) NOT NULL," \
                    "post_text varchar(150) NOT NULL" \
                    ");"
            cursor.execute(query)
            print("Table created successfully")

        with connection.cursor() as cursor:
            query = "CREATE TABLE tags (" \
                    "id int PRIMARY KEY," \
                    "tag_name varchar(50) NOT NULL" \
                    ");"
            cursor.execute(query)
            print("Table created successfully")

        with connection.cursor() as cursor:
            query = "CREATE TABLE posts_tags (" \
                    "post_id int REFERENCES posts(id)," \
                    "tag_id int REFERENCES tags(id)," \
                    "CONSTRAINT posts_tags_pk PRIMARY KEY (post_id, tag_id)" \
                    ");"
            cursor.execute(query)
            print("Table created successfully")




        #  #insert data
        # with connection.cursor() as cursor:
        #      insert_query = "INSERT INTO users (name, password, email) VALUES('Nata', 'ytrew', 'nata@g.com');"
        #      cursor.execute(insert_query)
        #      connection.commit()
        #
        # with connection.cursor() as cursor:
        #      insert_query = "INSERT INTO passports (passport_number, city_of_registration, fk_passport_users) VALUES(12345, 'Odessa', 1);"
        #      cursor.execute(insert_query)
        #      connection.commit()

        # #update data
        # with connection.cursor() as cursor:
        #     update_query = "UPDATE users SET password = 'xxxXXX' WHERE id = 1"
        #     cursor.execute(update_query)
        #     connection.commit()
        #
        # #delete data
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM users WHERE id = 1;"
        #     cursor.execute(delete_query)
        #     connection.commit()
        #
        #
        #
        # #select all data from table
        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT * FROM users"
        #     cursor.execute(select_all_rows)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
        #
        # #drop table
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE users"
        #     cursor.execute(drop_table_query)
        #



    finally:
        connection.close()
except Exception as ex:
    print("Connection refused...")
    print(ex)