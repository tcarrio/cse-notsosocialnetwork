from model.orm import Profile, Account
from model.database import db_session


def get_profile(session):
    if 'user' not in session:
        return Null
    return db_session.query(Post).\
    options(joinedload(Post.account_rel)).\
    filter(Post.account_email==session['user']).\
    order_by(Account.account_email).first()