#!/bin/bash

path="${0%/*/*}/user_interface"
cd $path
python3 task_checker.py
echo -e "\n\n\n"
cowsay -f moose "Good luck with your chores!"
sleep 16