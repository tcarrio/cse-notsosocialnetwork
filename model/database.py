from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.env_config import ProductionConfig as Conf
from model.orm import Account,Profile,Post,Message

engine = create_engine(Conf.DATABASE_URI, convert_unicode=True)

def get_new_session():
    return scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

db_session = get_new_session()
Base = declarative_base()
Base.query = db_session.query_property()
    
def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import model.orm.Account
    import model.orm.Profile
    import model.orm.Post
    import model.orm.Message
    Base.metadata.create_all(bind=engine)