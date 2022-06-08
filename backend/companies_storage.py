from flask import abort


class CompaniesStorage:
    def __init__(self):
        self.storage = {}

    def add(self, company, uid):
        if self.storage.get(uid):
            abort(400, f'uid {uid} already exists')
        self.storage[uid] = company

    def delete(self, uid):
        if not self.storage.get(uid):
            abort(404, f'uid {uid} not found')
        del self.storage[uid]

    def update(self, company, uid):
        if not self.storage.get(uid):
            abort(404, f'uid {uid} not found')
        self.storage[uid] = company   
        
    def get_by_id(self, uid):
        if not self.storage.get(uid):
            abort(404, f'uid {uid} not found')
        return self.storage[uid]

    def get_all(self):
        return self.storage