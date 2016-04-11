class Config(object):
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DATABASE_URI = 'sqlite:///tmp/nssn.db'
    
class ProductionConfig(Config):
    DATABASE_URI = 'mysql+pymysql://root:nssntest@localhost/nssndb'