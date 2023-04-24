from json_interface import json_interface as ji

page = ji.get_last_page()
check = ji.get_lat_check()

def today_plans(page,check):
    print("\n\nPlans for today:\n")
    for i, plan, check in zip(enumerate(page['plans'].values(), start=1),check):
        if bool(check):
            print(f"{i}. {plan}\n [x]")
        else:
            print(f"{i}. {plan}\n [ ]")

today_plans(page,check)
inp = input("\nHave you complete any task?\n(wich/n):").lower()
while not inp.startswith('n'):
    if int(inp) and int(inp)<8:
        check["plans_check"][f"plan_{inp}"] = 1
        today_plans(page,check)
        inp = input("\nHave you complete any other task?\n(wich/n):").lower()
    else:
        print('invalid task!')
        inp=('Invalid task, select another one!')
    
