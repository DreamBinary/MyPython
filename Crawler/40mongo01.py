from pymongo import *

client = MongoClient("mongodb://localhost:27017/")

db = client.pycrawler

coll = db.students

# student = {
#     "id": "1234",
#     "name": "abcd"
# }
# result = coll.insert_one(student)
# print(result)

# result = coll.find_one({"id": "123"})
# print(type(result))
# print(result)
# print("-----------")
# results = coll.find({"id": "1234"})
# for i in results:
#     print(i)

# condition = {"id": "cba"}
# student = coll.find_one(condition)
# print(student)
# print(type(student))
# student["id"] = "455"
# result = coll.update_one(condition, {"$set": student})
# print(result.matched_count, result.modified_count)

result = coll.delete_one({"id": "1234"})
print(result.deleted_count)