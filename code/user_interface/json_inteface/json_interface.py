import json
import jsonlines
import datetime

with open('path.txt') as f:
    base_path = f.readline()

JOURNAL_PATH = base_path + '/data/journal.jsonl'
TEMP_PAGE_PATH = base_path + '/data/temp_page.jsonl'
TASK_CHECKER_PATH = base_path + '/data/task_check.jsonl'
TEMP_CHECKER_PATH = base_path + '/data/temp_check.jsonl'

class Page(object):
    def __init__(self):
        self.page = self.get_last_page()
        self.date = self.page['date']
    
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
        
        
    
    def load_page(path):
        with open(path, 'r') as f:
            return json.load(f)
    
    def get_last_page():
        with jsonlines.open(JOURNAL_PATH) as reader:
            for page in reader:
                last_page = page
        return last_page



def write_temp_checker(temp_checker):
    with jsonlines.open(TEMP_CHECKER_PATH, mode='w') as writer:
        writer.write(temp_checker)
        print ('\nTemp checker saved!\n')
    return

def get_line_bydate(date,path):
    with jsonlines.open(path, reverse=True) as reader:
        for line in reader:
            if line['date'] == date:
                return line
    return None

class NewPage (Page):
    template_page_path = base_path + '/code/user_interface/json_interface/page_template.json'
    template_checker_path = base_path + '/code/user_interface/json_interface/checker_template.json'
    
    def __init__(self):
        self.page = self.load_page(self.template_page_path)
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.page['date']= self.date
        self.checker = self.load_page(TEMP_CHECKER_PATH)
        

    def write_jsonl(path,json_obj):
        with jsonlines.open(path, mode='a') as writer:
            writer.write(json_obj)
        return