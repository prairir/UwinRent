class Config(object):

    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# TODO
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://ryan@localhost:5432/UWinRent"
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    TESTING = True
