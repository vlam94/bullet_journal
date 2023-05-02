import datetime
from json_interface import json_interface as ji

PAGE_TEMPLATE_PATH = 'page_template.json'
CHECKER_TEMPLATE_PATH = 'checker_template.json'

def page_fill():
    page = ji.load_today_template(PAGE_TEMPLATE_PATH)
    
    page['good_things']['good_thing_1'] = input("What is one good thing that happened today? ")
    page['good_things']['good_thing_2'] = input("What is another good thing that happened today? ")
    page['good_things']['good_thing_3'] = input("What is one more good thing that happened today? ")

    page['improvements']['improvement_1'] = input("What is one thing you could have done differently today to improve it? ")
    page['improvements']['improvement_2'] = input("What is another thing you could have done differently today to improve it? ")
    page['improvements']['improvement_3'] = input("What is one more thing you could have done differently today to improve it? ")

    for plan in page['plans']:
        page['plans'][plan] = input(f"What is your {plan.replace('_', ' ')} for tomorrow? ")

    return page

def task_checker(page):
    checker = ji.load_page(ji.TEMP_CHECKER_PATH)
    for task in page['plans']:
        if not checker['plans_check'][task]:
            check = input(f"Did you completed '{page['plans'][task]}' as planned?\n(y/n)").lower().startswith('y')
            checker['plans_check'][task] = int(check)
    return checker

def rewrite_field(fieldcat,page):
    field = fieldcat.rstrip(fieldcat[-1]) + '_ '
    while True:
        fieldnum = input(f"\nWich {fieldcat[:-1]} would you like to re-enter?: ")
        field = field[:-1] + fieldnum
        try:     
            page[fieldcat][field] in page
            break
        except KeyError:
            print("\nOops!  Invalid index!")
    
    page[fieldcat][field] = input(f"\nre-type {field} bellow:\n")
    return
    

def page_checkout(page):
    ji.print_page (page)
    if input("\nWould you like to change anything?\n(y/n):").lower().startswith('n'):
        return
    field_type = input("\nWould you like to change a 'Good Thing'(G), 'Improvement'(I), 'Plan'(P)").upper()
    while field_type not in ['P','I','G']:
        field_type = input("\nInvalid Input!\nType 'G','I' or 'P' ").upper()
    if field_type.startswith('G'):
        rewrite_field('good_things',page)
    elif field_type.startswith('I'):
        rewrite_field('improvements',page)
    else:
        rewrite_field('plans',page)
    page_checkout(page)
        
  

yesterday = ji.get_last_page()
if yesterday:
    task_check = task_checker(yesterday)
page = page_fill()
print("\n\nHere's a preview of the page:\n")
page_checkout(page)
ji.write_jsonl(ji.JOURNAL_PATH, page)
ji.write_jsonl(ji.TASK_CHECKER_PATH, task_check)
ji.write_temp_checker(ji.load_today_template(CHECKER_TEMPLATE_PATH))
print("Nice job!\nEntry complete for today!")

#json file review
ji.print_page(ji.get_last_page())