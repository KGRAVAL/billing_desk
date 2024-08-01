import mysql.connector
# from query_module import QueryModule as qry
import os
# P@ssword.123
# ALTER USER 'root'@'localhost' IDENTIFIED BY 'newPass@123';

class Database:
    # Database connection credentials
    def __init__(self, host, user, password,dbname):
        self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database = dbname)
        self.cur = self.conn.cursor()

        # user_col = (user_id NOT NULL , admin_name, admin_pass, admin_gender ,admin_dob , admin_city, admin_job,user_status)
        # qry.create_table("user_table",user_col)
        def execute_query(self,query):
            self.cur.execute(query) 
            self.conn.commit() 
        
        
        # query1 = '''(CREATE TABLE IF NOT EXISTS 'quick_cart_hub'.'user_table' ('ID' INT NOT NULL AUTO_INCREMENT,
        #                         'user_id' VARCHAR(20) NOT NULL,
        #                         'user_name' VARCHAR(45) NOT NULL,
        #                         'user_password' VARCHAR(45) NOT NULL,
        #                         'gender' TINYINT NOT NULL,
        #                         'dob' DATETIME NOT NULL,
        #                         'city' VARCHAR(45) NULL,
        #                         'date_joining' DATETIME NOT NULL,
        #                         'is_admin' TINYINT NULL DEFAULT 1,
        #                         'is_aproved' TINYINT NULL DEFAULT 0,
        #                         PRIMARY KEY ('user_id'),
        #                         UNIQUE INDEX 'user_id_UNIQUE' ('user_id' ASC) VISIBLE,
        #                         UNIQUE INDEX 'ID_UNIQUE' ('ID' ASC) VISIBLE);)'''
        # query2 = '''(CREATE TABLE IF NOT EXISTS 'quick_cart_hub'.'categories' (
        #                                         'cate_id' INT NOT NULL,
        #                                         'cate_name' VARCHAR(45) NOT NULL,
        #                                         PRIMARY KEY ('cate_id'),
        #                                         UNIQUE INDEX 'cate_id_UNIQUE' ('cate_id' ASC) VISIBLE);)'''
        # execute_query(query1)
        # execute_query(query2)
    
