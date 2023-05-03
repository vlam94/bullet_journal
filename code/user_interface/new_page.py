from json_interface import NewPage, Page

current = Page()
current.task_checker()
current.append_to_journal()
new = NewPage()
new.page_fill()
new.write_temp()
print("Nice job!\nEntry complete for today!")