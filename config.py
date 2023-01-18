class Config(object):
    DEBUG = True
    SECRET_HERE = '1337'
    SQLALCHEMY_DATABASE_URI = "sqlite:///./movies.db"
    SQLALCHEMY_TRACK_MODIFICATION = False