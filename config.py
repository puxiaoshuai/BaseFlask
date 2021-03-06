import os

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'base_flask'
USENAME = 'root'
PASSWORD = 'xxxx'
DB_URI = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(USENAME, PASSWORD, HOSTNAME, PORT, DATABASE)
PAGE_SIZE = 9


class BaseConfig(object):
    # SECRET_KEY=os.urandom(24)
    SECRET_KEY = 'makesure to set a very secret key'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
