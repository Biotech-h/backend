import itertools

class JobStorage:

    def __init__(self):
        self.storage = {}
        self.uid = itertools.count(1)

    def add(self, job):
        job['uid'] = next(self.uid)
        uid = job["uid"]
        self.storage[uid] = job
        return job

    def delete(self, uid):
        if not self.storage.get(uid):
            raise ValueError(f'uid {uid} not found')
        del self.storage[uid]

    def update(self, job):
        uid = job['uid']
        if not self.storage.get(uid):
            raise ValueError(f'uid {uid} not found')
        self.storage[uid] = job
        return job

    def get_by_id(self, uid):
        if not self.storage.get(uid):
            raise ValueError(f'uid {uid} not found')
        return self.storage[uid]

    def get_all(self):
        return self.storage.values()
