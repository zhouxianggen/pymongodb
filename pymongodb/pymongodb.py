# coding: utf8
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from pyobject import PyObject


class PyMongoDb(PyObject):
    def __init__(self, host, port, user, pswd, db, maxPoolSize=20):
        super(PyMongoDb, self).__init__()
        client = MongoClient(host, port, maxPoolSize=maxPoolSize)
        if pswd:
            client.admin.authenticate(user, pswd)
        self.db = client[db]
        self.collections = set()

    def save(self, doc):
        collection = 'col_%s' % datetime.datetime.now().strftime('%Y%m%d')
        self.create_collection(collection)
        if collection not in self.collections:
            return None
        try:
            ret = self.db[collection].insert_one(doc)
        except Exception as e:
            self.log.exception(e)
            return None
        return (collection, ret.inserted_id)

    def get(self, collection, _id):
        docs = self.find(collection, {'_id': ObjectId(_id)})
        return docs[0] if docs else None

    def update(self, collection, _id, update):
        try:
            ret = self.db[collection].replace_one(
                    {'_id': ObjectId(_id)}, update)
        except Exception as e:
            self.log.exception(e)
            return 0
        return ret.modified_count

    def find(self, collection, filter):
        if collection not in self.db.collection_names():
            return []
        cursor = self.db[collection].find(filter)
        return [doc for doc in cursor]

    def create_collection(self, collection):
        if collection in self.collections:
            return
        if collection in self.db.collection_names():
            self.collections.add(collection)
            return
        try:
            self.db.create_collection(collection)
            self.collections.add(collection)
        except Exception as e:
            self.log.exception(e)

