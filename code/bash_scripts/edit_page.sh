#!/bin/bash

path="${0%/*/*}/user_interface"
cd $path
python3 page_checkout.py
cowsay -f moose "page successfully edited!!!"
sleep (15)