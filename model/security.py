import hashlib

class Hasher():
    def __init__(self):
        self.about = "I hash passwords sent from the webpage. No puns. Sorry D:"
    def get_hash(password=None):
        if not password:
            return None
        return hashlib.sha512(password.encode('utf-8')).hexdigest()[:64]