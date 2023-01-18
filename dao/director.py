from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, dir_dic):
        new_director = Director(**dir_dic)
        self.session.add(new_director)
        self.session.commit()
        return new_director

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, dir_dic):
        director = self.get_one(dir_dic('id'))
        director.name = dir_dic.get('name')

        self.session.add(director)
        self.session.commit()


