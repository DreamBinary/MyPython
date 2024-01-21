import pymysql

db = pymysql.connect(host="localhost", user="root", password="mysqlcxq", port=3306)
# try:
#     cursor = db.cursor()
#     cursor.execute("select * from west.goods;")
#     datas = cursor.fetchall()
#     for i in datas:
#         print(i)
# except:
#     print("-------")

# try:
#     cursor = db.cursor()
#     sql = """insert into `west`.goods
# (商品编号, 商品名, 商品价格)
# values
# ('10027', '哈哈', 520)"""
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#     print("-------")


cursor = db.cursor()
data = {
    "id": "14",
    "name": "哇哇",
    "pwd": "123456"
}
table = "mybatis.user"
keys = ",".join(data.keys())
values = ",".join(["'%s'"] * len(data))

# values = ",".join(data.values())
# values = "'15','哇哇','123456'"
sql = "insert into {table} ({keys}) values ({values})".format(table=table, keys=keys, values=values) % tuple(data.values())
print(sql)
try:
    if cursor.execute(sql):
        print("^^^^")
        db.commit()
except:
    print("------")
    db.rollback()


db.close()
