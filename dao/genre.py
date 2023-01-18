from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, gen_dic):
        new_genre = Genre(**gen_dic)
        self.session.add(new_genre)
        self.session.commit()
        return new_genre

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, gen_dic):
        genre = self.get_one(gen_dic('id'))
        genre.name = gen_dic.get('name')

        self.session.add(genre)
        self.session.commit()


