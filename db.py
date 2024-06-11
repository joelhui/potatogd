# db.py

import pymysql

class Mysql(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host="localhost", user="root", password="123456", database="test")
            self.cursor = self.db.cursor()
            print("connect successful！")
        except Exception as e:
            print(f"connect failed！{e}")

    def getdata(self):
        # print("query database")
        sql = "select * from curation"

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        # print("           ",results)
        return results

    def insert_data(self, data):
        # print("insert ……")
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO curation ({keys}) VALUES ({values})"

        try:
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
            self.db.rollback()

    def update_data(self, id, data):
        # print("update……")

        set_clause = ', '.join([f"{key}=%s" for key in data])
        sql = f"UPDATE curation SET {set_clause} WHERE id=%s"

        values = list(data.values()) + [id]
        try:
            self.cursor.execute(sql, tuple(values))
            self.db.commit()
        except Exception as e:
            print(f"Error updating data: {e}")
            self.db.rollback()

    def delete_data(self, id):
        print("delete")
        sql = "DELETE FROM curation WHERE id=%s"
      
        try:
            self.cursor.execute(sql, (id,))
            self.db.commit()
        except Exception as e:
            print(f"Error deleting data: {e}")
            self.db.rollback()

    def __del__(self):
        self.db.close()
