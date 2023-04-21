#!/bin/bash

cd /home/vlam94/bullet_journal/code/user_interface
python3 new_page.py
tail -n 1 /home/vlam94/bullet_journal/data/journal.jsonl | python3 -c 
'import json,sys;
obj=json.load(sys.stdin);
print("Title: "+obj["title"]+"\n"+"Content: "+obj["content"]+"\n"+"Created: "+obj["created"]+"\n"+"Tags: "+",".join(obj["tags"]))'
sleep 15
