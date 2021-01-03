import pymysql
from Flask_end_to_end.helper.app_queries import *


def get_connection():
    return pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD,
                 database=DB_NAME, port=PORT)



if __name__ == '__main__':
    conn=get_connection()
    print(conn)