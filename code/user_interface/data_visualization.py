from json_interface import PagebyDate


while True:
    inp = input("Select a Date in Format 'yyyy-mm-dd' or 'e' to exit:\n")
    if inp.upper().startswith('E'):
        break
    page = PagebyDate(inp)
    if page.page:
        print(page)