from CheckoutPage import *

class PagebyDate (CheckoutPage):
    def __init__(self,date):
        self.date = date
        while not datetime.strptime(self.date,'%Y-%m-%d'):
            self.date = input("Wrong format!!! use 'yyyy-mm-dd':\n")
        self.page = self.get_line_bydate(JOURNAL_PATH)
        self.checker = self.get_line_bydate(TASK_CHECKER_PATH)

    def get_line_bydate(self,path):
        with jsonlines.open(path) as reader:
            for line in reader:
                if line['date'] == self.date:
                    return line
        print (f"date {self.date} not found")
        return None

