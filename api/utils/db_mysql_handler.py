"""
1. connect to DB
2. get one record
3. get records number
4. get all records
5. close connections
"""
import pymysql

from api.utils.config_handler import conf


class HandleDB(object):

    def __init__(self, host, port, user, password, database):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset="utf8",
            # change result format to dict
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def get_one_record(self, sql):
        self.conn.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_all_records(self, sql):
        self.conn.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_count(self, sql):
        self.conn.commit()
        return self.cursor.execute(sql)

    def close_connections(self):
        self.cursor.close()
        self.conn.close()

    def update(self, sql):
        """
        CRUB,
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        self.conn.commit()


handle_db = HandleDB(
        conf.get("mysql", "host"),
        int(conf.get("mysql", "port")),
        conf.get("mysql", "user"),
        conf.get("mysql", "password"),
        conf.get("mysql", "database")
    )


if __name__ == '__main__':
    # handle_db = HandleDB(
    #     conf.get("mysql", "host"),
    #     int(conf.get("mysql", "port")),
    #     conf.get("mysql", "user"),
    #     conf.get("mysql", "password"),
    #     conf.get("mysql", "database")
    # )
    sql = "select * from tb_users LIMIT 3"
    print(handle_db.get_one_record(sql))
    print(handle_db.get_all_records(sql))
    handle_db.close_connections()
