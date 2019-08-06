# -*- coding: utf-8 -*-
import os
import psycopg2

class Postgres:
    
    # DBと接続
    def get_connection(self):
        return psycopg2.connect(os.environ["DATABASE_URL"])
        
    # 新規登録            
    def insert(self, user_id=None, channel_id=None, feed_url=None):
        query = "INSERT INTO user_info (user_id, channel_id) VALUES('%s', '%s');"
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query % (user_id, channel_id))
 
