from json_interface import json_interface as ji

page = ji.get_last_page()
print("\n\nPlans for today:\n")
for i, plan in enumerate(page['plans'].values(), start=1):
    print(f"{i}. {plan}\n")
