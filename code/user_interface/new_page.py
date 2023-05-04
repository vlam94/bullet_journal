from json_interface import Page, NewPage

current = Page()
current.check_task()
current.append_to_journal()
new = NewPage()
new.page_fill()
new.write_temp()
print("Nice job!\nEntry complete for today!")