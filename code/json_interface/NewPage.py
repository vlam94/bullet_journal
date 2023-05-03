from Page import *

class NewPage (Page):
 
    def __init__(self):
        self.page = self.load_page(TEMPLATE_PAGE_PATH)
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.page['date'] = self.date
        self.checker = self.load_page(TEMPLATE_CHECKER_PATH)
        self.checker['date'] = self.date


    def page_fill(self):
        self.page['good_things']['good_thing_1'] = input("What is one good thing that happened today? ")
        self.page['good_things']['good_thing_2'] = input("What is another good thing that happened today? ")
        self.page['good_things']['good_thing_3'] = input("What is one more good thing that happened today? ")

        self.page['improvements']['improvement_1'] = input("What is one thing you could have done differently today to improve it? ")
        self.page['improvements']['improvement_2'] = input("What is another thing you could have done differently today to improve it? ")
        self.page['improvements']['improvement_3'] = input("What is one more thing you could have done differently today to improve it? ")

        for plan in self.page['plans']:
            self.page['plans'][plan] = input(f"What is your {plan.replace('_', ' ')} for tomorrow? ") 
            