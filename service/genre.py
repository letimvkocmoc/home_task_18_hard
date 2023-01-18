from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        genres = self.dao.get_all()
        return genres

    def create(self, gen_dic):
        return self.dao.create(gen_dic)

    def update(self, gen_dic):
        self.dao.update(gen_dic)
        return self.dao

    def delete(self, gid):
        self.dao.delete(gid)
