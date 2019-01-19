from utils import SPLITTER
import datetime

DATE_FORMAT = '%Y-%m-%d'

class CommitData:

    def __init__(self,branch):
        self.branch = branch
    
    def __str__(self):
        return " >>>> {} - {}".format(self.date,self.branch)

    def set_date(self,date):
        self.date = datetime.datetime.fromtimestamp(int(date))
    
    def get_date(self):
        return self.date
