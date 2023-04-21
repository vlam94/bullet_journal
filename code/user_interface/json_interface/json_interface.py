import json
import jsonlines


JOURNAL_PATH = '../../data/journal.jsonl'
TASK_CHECKER_PATH = '../../data/task_check.jsonl'

def load_page_template(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_last_page():
    with jsonlines.open(JOURNAL_PATH) as reader:
        for page in reader:
            last_page = page
    return last_page

def write_jsonl(path,json_obj):
    with jsonlines.open(path, mode='a') as writer:
        writer.write(json_obj)
        writer.write()
    return

def print_page(page):
    # Print the date
    print(f"Date: {page['date']}\n")

    # Print the good things
    print("Good Things:")
    for i, good_thing in enumerate(page['good_things'].values(), start=1):
        print(f"{i}. {good_thing}")
    print()

    # Print the improvements
    print("Improvements:")
    for i, improvement in enumerate(page['improvements'].values(), start=1):
        print(f"{i}. {improvement}")
    print()

    # Print the plans
    print("Plans:")
    for i, plan in enumerate(page['plans'].values(), start=1):
        print(f"{i}. {plan}\n")

def get_line_bydate(date,path):
    with jsonlines.open(path, reverse=True) as reader:
        for line in reader:
            if line['date'] == date:
                return line
    return None

