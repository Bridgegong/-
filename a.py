#conding='utf-8'
# import pymongo
# client = pymongo.MongoClient('192.168.20.115', 27017)
# wens = client['wens']['table']
# dict1 ={'id':1,

#         'age': 26,
#         }
# wens.insert_one(dict1)

# class MongodbConn(object):
#
#     def __init__(self):
#         self.CONN = pymongo.MongoClient('192.168.20.115', 27017)
#
#     def run(self):
#         database = "test"
#         db = self.CONN[database]
#         db.authenticate("nlp", "nlp")
#         col = db.collection_names()[3]
#         print(db.collection_names())
#         collection = db.get_collection(col)
#         print(collection)
#
# if __name__ == '__main__':
#     mo = MongodbConn()
#     mo.run()

f = open('a.txt','a+')
f.write('贡桥锋')
