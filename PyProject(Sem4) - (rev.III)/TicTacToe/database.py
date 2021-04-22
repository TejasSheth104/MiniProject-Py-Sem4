# database

import mysql.connector

def database(name,result):

    if result==1:
        sql_query  = "INSERT INTO record (PLAYER_NAME,WIN) VALUES ();"
        sql_query2 = "SELECT WIN FROM tic_tac_toe.record WHERE PLAYER_NAME=%s"
        val=(name)
    elif result==2:
        sql_query  = "INSERT INTO record (PLAYER_NAME,LOSS) VALUES ();"
        sql_query2 = "SELECT LOSS FROM tic_tac_toe.record WHERE PLAYER_NAME=%s"
        val=(name)
    elif result==3:
        sql_query  = "INSERT INTO record (PLAYER_NAME,DRAW) VALUES ();"
        sql_query2 = "SELECT DRAW FROM tic_tac_toe.record WHERE PLAYER_NAME=%s"
        val=(name)

    try:
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="tejas1004",   
                auth_plugin="mysql_native_password",
                database="Tic_Tac_Toe")

        if conn.is_connected():
            # print("MySQL Connection Established.")
            cursor = conn.cursor()

# CREATE TABLE
            # cursor.execute(
            #     '''CREATE TABLE Record (
            #         PLAYER_ID int unique not null autoincrement,
            #         PLAYER_NAME varchar(50),
            #         WIN int,
            #         LOSS int,
            #         DRAW int
            #         );'''
            # )

# UPDATE TABLE
            cursor.execute()
            conn.commit()

    except:
        print("MySQL Connection Failed or Table Already Exists.")
        exit()

    # cursor.execute("SHOW TABLES;")
    # for table_name in cursor:
    #     print(table_name)

    if conn.is_connected():
        cursor.close()
        conn.close()
        # print("MySQL Connection Terminated.")

# 1- win
# 2- loss
# 3- draw
name='Tejas'
result=1
database(name,result)