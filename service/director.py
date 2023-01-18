from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        directors = self.dao.get_all()
        return directors

    def create(self, dir_dic):
        return self.dao.create(dir_dic)

    def update(self, dir_dic):
        self.dao.update(dir_dic)
        return self.dao

    def delete(self, did):
        self.dao.delete(did)
