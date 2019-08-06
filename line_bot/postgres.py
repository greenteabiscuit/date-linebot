# -*- coding: utf-8 -*-
import os
import psycopg2

class Postgres:
    
    # DBと接続
    def get_connection(self):
        return psycopg2.connect(os.environ["DATABASE_URL"])
        
    # 新規登録            
    def register_user(self, user_id = None):
        query = "INSERT INTO user_info (user_id) VALUES('%s');"
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query % user_id)
    
    def get_users(self, channel_id):
        query = "SELECT (user_id FROM user_info ;"
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
            
    """            
    def create_table(self):
        query="CREATE TABLE user_info (id serial, user_id varchar(50) NOT NULL);"
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
    """
