class Config(object):

    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# TODO
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://<USR>:<PASSWD>@<URL>:<PORT>/<DBNAME>"
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://<USR>:<PASSWD>@<URL>:<PORT>/<DBNAME>"
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    TESTING = True
