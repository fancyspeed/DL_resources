import pprint
import datetime
from pymongo import MongoClient

m_client = MongoClient('localhost', 27017)
m_db = m_client.gaotao
m_raw_doc = m_db.raw_doc

raw_doc = {"author": "Mike",
      "text": "My first blog post!",
      "tags": ["mongodb", "python", "pymongo"],
      "date": datetime.datetime.utcnow()}

post_id = m_raw_doc.insert_one(raw_doc).inserted_id

pprint.pprint(m_raw_doc.find_one({"author": "Mike"}))

#insert_many
#for post in posts.find
#result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],unique=True)
#sorted(list(db.profiles.index_information()))
