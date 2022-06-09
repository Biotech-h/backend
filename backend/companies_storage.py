from backend.errors import ConflictError, NotFoundError


class CompaniesStorage:
    name = 'companies'

    def __init__(self):
        self.storage = {}

    def add(self, company):
        uid = company['uid']
        if self.storage.get(uid):
            raise ConflictError(self.name, f'uid {uid} already exists')

        self.storage[uid] = company
        return company

    def delete(self, uid):
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f'uid {uid} not found')

        del self.storage[uid]

    def update(self, company):
        uid = company['uid']
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f'uid {uid} not found')

        self.storage[uid] = company
        return company

    def get_by_id(self, uid):
        if not self.storage.get(uid):
            raise NotFoundError(self.name, f'uid {uid} not found')

        return self.storage[uid]

    def get_all(self):
        return self.storage.values()
