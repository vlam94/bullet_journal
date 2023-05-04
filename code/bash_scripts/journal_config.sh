#!/bin/bash

if [$(pwd|grep bash_scripts)]
then
    scripts_path=$(pwd)
else
    echo "run this script from within it's folder (.../bullet_journal/code/bash_scripts)"
    exit
fi
cd ..; cd ..
if [  -d "data" ]
then
    cowsay -f moose "bullet journal configured!"
    exit
fi
mkdir data
touch data/journal.jsonl
touch data/checker.jsonl
touch data/temp_checker.jsonl
cd ~
sudo echo "#created on bullet journal configuration:" >> .bashrc
sudo echo 'export PATH=$PATH:'$script_path >> .bashrc
sudo apt install cowsay -y
cowsay -f moose "bullet journal configured!"
