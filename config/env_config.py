class Config(object):
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DATABASE_URI = 'sqlite:///tmp/nssn.db'
    WEB_PORT = 5000
    WEB_HOST = 'localhost'
    SESSION_TYPE = 'memcached'
    SECRET_KEY = '@NYpQe#Bm*0iT3KcT0n%EuuGDZ^vkWA%6XSoeRqWAfOUMkLph0phbw8FKaA%VwPB'
    
class ProductionConfig(Config):
    DATABASE_URI = 'mysql+pymysql://nssnuser:2rU9ZFnd2xYMilSb@nssn.carrio.me/nssndb'
    WEB_PORT = 80
    WEB_HOST = 'nssn.carrio.me'
    SESSION_TYPE = 'memcached'
    SECRET_KEY = '@NYpQe#Bm*0iT3KcT0n%EuuGDZ^vkWA%6XSoeRqWAfOUMkLph0phbw8FKaA%VwPB'
    EXT_IP = "localhost"#'nssn.carrio.me'