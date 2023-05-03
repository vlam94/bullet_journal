import json
import jsonlines
from datetime import datetime

#setting file pathes
#with open('path.txt') as f:
#    base_path = f.readline()
base_path = '/home/vlam94/bullet_journal'
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
    
    def task_checker(self):
        for task in self.page['plans']:
            if not self.checker['plans_check'][task]:
                check = input(f"Did you completed '{self.page['plans'][task]}' as planned?\n(y/n)").lower().startswith('y')
                self.checker['plans_check'][task] = int(check)
    