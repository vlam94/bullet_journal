#!/bin/bash

path="${0%/*/*}/user_interface"
cd $path
python3 new_page.py
python3 page_checkout.py
sleep 15
