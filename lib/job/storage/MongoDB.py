from lib.job.storage.Storage import Storage
from pymongo import MongoClient
from time import time


class MongoDB(Storage):

    def __init__(self, job_name, storage_config):
        super(MongoDB, self).__init__()
        connection = MongoClient(storage_config['host'], storage_config['port'])
        self.collection = connection.job[job_name]

    def add(self, job):
        task = {
            'request': job,
            'created': time(),
            'status': self.STATUS_ACTIVE
        }
        self.collection.insert_one(task)

    def get_active(self):
        return self.collection.find({'status': self.STATUS_ACTIVE})

    def get_one_active(self):
        return self.collection.find_one({'status': self.STATUS_ACTIVE})

    def get_in_progress(self):
        return self.collection.find({'status': self.STATUS_IN_PROGRESS})

    def get_complete(self):
        return self.collection.find({'status': self.STATUS_COMPLETE})

    def as_active(self, id):
        self._update_status(id, self.STATUS_ACTIVE)

    def as_in_progress(self, id):
        self._update_status(id, self.STATUS_IN_PROGRESS)

    def as_complete(self, id):
        self._update_status(id, self.STATUS_COMPLETE)

    def _update_status(self, id, status):
        self.collection.update_one({'_id': id}, {'$set': {'status': status}})

    def clear(self):
        self.collection.delete_many({})