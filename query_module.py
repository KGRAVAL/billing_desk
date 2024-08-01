import mysql
import mysql.connector
from conn_db import Database

class QueryModule:
    def __init__(self):
        self.dbname = "quick_cart_hub"
        self.db = Database()
    
    def use_db(self, db_name):
        scr_use_db = (f"USE {db_name}")
        self.db.execute_query(scr_use_db)
        print(f"You are using database : {db_name}")
   
    def create_table(self,table_name,col_name):
        scr_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} ({col_name});"
        self.db.execute_query(scr_create_table)
        print(f"Table is created with name {table_name}")
        # show_table(self,table_name)
    
    def insert_table(self,table_name,values):
        QueryModule.create_table(table_name,values)     
        scr_insert = f"INSERT INTO {table_name} VALUES (values);"
        self.db.execute_query(scr_insert)
        print(f"Values inserted into table {table_name} successfully.")

    def check_admin_exists(self,user_id):
        scr_user_exixtance = f"SELECT user_id FROM user_table WHERE user_id = '{user_id}';"
        self.db.execute_query(scr_user_exixtance)
        # return False

    def select_in_table(self,table_name,condition):
        scr_select = f"SELECT * FROM user_table WHERE {condition};"
        self.db.execute_query(select_in_table)
        
    def log_varify(cols,table_name,condition):
        scr_select = f"SELECT {cols} FROM {table_name} WHERE {condition};"
        if scr_select:
            return False
# execute_query(self,query)   
# select user_id from table user_table 
# select * from user 