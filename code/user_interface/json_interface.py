import json
import jsonlines
from datetime import datetime

base_path = '/'
for parse in str(__file__)[1:].split('/'):
    base_path += parse
    if parse == 'bullet_journal':
        break
    base_path += '/'
#journal archive
JOURNAL_PATH = base_path + '/data/journal.jsonl'
TASK_CHECKER_PATH = base_path + '/data/task_check.jsonl'
#current day's page
TEMP_PAGE_PATH = base_path + '/data/temp_page.jsonl'
TEMP_CHECKER_PATH = base_path + '/data/temp_check.jsonl'
#templates
TEMPLATE_PAGE_PATH = base_path + '/code/user_interface/page_template.json'
TEMPLATE_CHECKER_PATH= base_path + '/code/user_interface/checker_template.json'

class Page(object):
    
    def __init__(self):
        self.page = self.load_page(TEMP_PAGE_PATH)
        self.checker = self.load_page(TEMP_CHECKER_PATH)
    
    def __str__ (self):
        #Starts ret string with date
        ret = f"\nDate: {self.page['date']}\n"

        # add the good things
        ret += "\nGood Things:"
        for i, good_thing in enumerate(self.page['good_things'].values(), start=1):
            ret += f"\n{i}. {good_thing}"
    
        # add the improvements
        ret += ("\n\nImprovements:")
        for i, improvement in enumerate(self.page['improvements'].values(), start=1):
            ret += f"\n{i}. {improvement}"
        
        #add the plans
        ret+= ("\nPlans:")
        for i, plan in enumerate(self.page['plans'].values(), start=1):
            ret += f"\n{i}. {plan}\n"
        
        ret += "\n\n"
        return ret
    
    def append_to_journal(self):
        with jsonlines.open(JOURNAL_PATH, mode='a') as writer:
            writer.write(self.page)
        with jsonlines.open(TASK_CHECKER_PATH, mode='a') as writer:
            writer.write(self.checker) 
        print("Entry Saved to Journal!")
    
    def write_temp(self):
        with jsonlines.open(TEMP_PAGE_PATH, mode = 'w') as writer:
            writer.write(self.page)
        with jsonlines.open(TEMP_CHECKER_PATH, mode = 'w') as writer:
            writer.write(self.checker)
        print ('\nTemp Page Saved!\n')

    def load_page(self,path):
        with open(path, 'r') as f:
            return json.load(f)
    
    def check_task(self):
        for task in self.page['plans']:
            if not self.checker['plans_check'][task]:
                check = input(f"Did you completed '{self.page['plans'][task]}' as planned?\n(y/n)").lower().startswith('y')
                self.checker['plans_check'][task] = int(check)
    

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


class CheckerPage (Page):

    def __str__(self):
        ret = "\n\nPlans for today:\n"
        it = [*zip(self.page['plans'].values(),self.checker['plans_check'].values())]
        for i, [plan, check] in enumerate(it, start=1):
            if check:
                ret+= f"{i}. {plan} [x]\n"
            else:
                ret+= f"{i}. {plan} [ ]\n"
        return ret
    
    def check_task(self): 
        print('\nHere are the updated plans for today:\n')
        print(self)
        inp = input("\nHave you complete any task?\n(which/n): ").lower() 
        self.task_mark_done(True,inp)

    def task_mark_done(self,done,inp):
        try:
            inp=int(inp)
            self.checker["plans_check"][f"plan_{inp}"] = int(done)
            print(self)
        except ValueError:
            if done:
                inp = input("Do you wish to unmark any mistaken task?\n(which/n)").lower()
                self.task_mark_done(False,inp)
            return   
        except IndexError: 
            inp = input('Invalid task! Select from 1 to 7: ').lower()
            self.task_mark_done(done,inp)
        inp = input("\nDo you want to update another task?\n(which/n): ").lower()    
        self.task_mark_done(done,inp)


class CheckoutPage(CheckerPage):      
    
    def __str__(self):
        ret = '\nUpdated Page\n'
        ret += f"\nDate: {self.page['date']}\n"
        ret += "\nGood Things:"
        for i, good_thing in enumerate(self.page['good_things'].values(), start=1):
            ret += f"\n{i}. {good_thing}"
        ret += ("\n\nImprovements:")
        for i, improvement in enumerate(self.page['improvements'].values(), start=1):
            ret += f"\n{i}. {improvement}"
        ret += CheckerPage.__str__(self)
        return ret
    
    def rewrite_field(self,fieldcat):
        field = fieldcat.rstrip(fieldcat[-1]) + '_ '
        while True:
            fieldnum = input(f"\nWich {fieldcat[:-1]} would you like to re-enter?: ")
            field = field[:-1] + fieldnum
            try:     
                self.page[fieldcat][field] in self.page
                break
            except KeyError:
                print("\nOops!  Invalid index!")
    
        self.page[fieldcat][field] = input(f"\nre-type {field} bellow:\n")
        return
    
    def checkout(self):
        print(self)
        if input("\nWould you like to change anything?\n(y/n):").lower().startswith('n'):
            return
        field_type = input("\nWould you like to change a 'Good Thing'(G), 'Improvement'(I), 'Plan'(P) or 'Check'(C)").upper()
        while field_type not in ['P','I','C','G']:
            field_type = input("\nInvalid Input!\nType 'G','I','P','C' ").upper()
        if field_type.startswith('G'):
            self.rewrite_field('good_things')
        elif field_type.startswith('I'):
            self.rewrite_field('improvements')
        elif field_type.startswith('P'):
            self.rewrite_field('plans')
        else:
            self.task_checker()
        self.checkout()


class PagebyDate (CheckoutPage):
    def __init__(self,date):
        self.date = date
        while True:
            try: 
                datetime.strptime(self.date,'%Y-%m-%d')
                break
            except ValueError:
                self.date = input("Wrong format!!! use 'yyyy-mm-dd':\n")
        self.page = self.get_line_bydate(JOURNAL_PATH)
        if self.page:
            self.checker = self.get_line_bydate(TASK_CHECKER_PATH)

    def get_line_bydate(self,path):
        with jsonlines.open(path) as reader:
            for line in reader:
                if line['date'] == self.date:
                    return line
        print (f"\ndate {self.date} not found!\n\n")
        return None