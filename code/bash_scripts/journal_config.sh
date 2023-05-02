#!/bin/bash

cd .. && cd ..
bullet_path=$(pwd)
mkdir data
touch data/journal.jsonl
touch data/checker.jsonl
touch data/temp_checker.jsonl
echo $bullet_path > code/user_interface/json_inteface/path.txt
chmod -w code/user_interface/json_inteface/path.txt
cd ~
sudo echo "#created on bullet journal configuration:" >> .bashrc
sudo echo 'export PATH=$PATH:'$bullet_path/code/bash_scripts >> .bashrc
sudo apt install cowsay -y
cowsay -f moose "bullet journal configured!"
