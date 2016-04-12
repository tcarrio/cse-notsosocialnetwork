class Config(object):
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DATABASE_URI = 'sqlite:///tmp/nssn.db'
    WEB_PORT = 5000
    WEB_HOST = 'localhost'
    
class ProductionConfig(Config):
    DATABASE_URI = 'mysql+pymysql://nssnuser:nssnpass@nssn.carrio.me/nssndb'
    WEB_PORT = 80
    WEB_HOST = 'nssn.carrio.me'