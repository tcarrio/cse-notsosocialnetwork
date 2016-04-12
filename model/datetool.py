import datetime

class DateHelper():
    def __init__(self):
        self.about="I make dates for the the database. No I can't get you a date, kid"
                
    def get_db_date(dobd,dobm,doby):
        print('About to parse')
        return datetime.datetime.strptime("{}/{}/{}".format(dobd,dobm,doby), "%d/%m/%Y")