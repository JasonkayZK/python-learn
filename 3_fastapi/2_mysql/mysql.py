import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="<pass>", db="testdb")
cur = conn.cursor()
cur.execute("SELECT Host, User FROM user")
for r in cur:
    print(r)
cur.close()
conn.close()
