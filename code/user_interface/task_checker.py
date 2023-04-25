from json_interface import json_interface as ji

page = ji.get_last_page()
check = ji.load_page(ji.TEMP_CHECKER_PATH)

def today_plans(page,check):
    print("\n\nPlans for today:\n")
    it = [*zip(page['plans'].values(),check['plans_check'].values())]
    for i, [plan, check] in enumerate(it, start=1):
        if bool(check):
            print(f"{i}. {plan} [x]\n")
        else:
            print(f"{i}. {plan} [ ]\n")


def task_mark_done(done,inp):
    try:
        inp=int(inp)
    except ValueError:
        return
    if inp<8:
        check["plans_check"][f"plan_{inp}"] = int(done)
        today_plans(page,check)
        print("\nDo you want to update another task?\n(which/n):",end="")
    else:
        print('Invalid task! Select from 1 to 7: ', end="")
    inp = input().lower()
    task_mark_done(done,inp)

today_plans(page,check)
inp = input("\nHave you complete any task?\n(which/n):").lower()
try:
    inp=int(inp)
except ValueError:
    exit()
task_mark_done(True,inp)
inp = input("Do you wish to correct(unmark) any task?\n(which/n)").lower()
task_mark_done(False,inp)
ji.write_temp_checker(check) 
print('\nHere are the updated plans for today:\n')
today_plans(page,ji.load_page(ji.TEMP_CHECKER_PATH))    
    
