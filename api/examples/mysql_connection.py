

"""
pip install pymysql

DB operation steps,
1. connect to DB, create cursor
2. SQL execution
3. fetch search result(s)
4. close connections
"""
import pymysql

# 1. connect to DB
conn = pymysql.connect(
    host="192.168.1.152",
    port=3306,
    user="alex",
    password="123456",
    database="mall",
    charset="utf8",
    # change result format to dict
    cursorclass=pymysql.cursors.DictCursor
)
# create a cursor
cursor = conn.cursor()

# 2. sql execution
sql = "select * from tb_users"
count = cursor.execute(sql)
print(count)

# 3. fetch results
data = cursor.fetchone()
print("The first record: ", data)
data = cursor.fetchone()
print("The second record: ", data)

# fetch all left records
all_data = cursor.fetchall()
print(all_data)

# no records
sql_no = "select * from tb_users where username='XXXXX'"
print(cursor.execute(sql_no))

# 4. close connections
cursor.close()
conn.close()