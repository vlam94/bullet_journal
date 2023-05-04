#!/bin/bash

journal_path="${0%/*/*}/data/journal.jsonl"
last_page=$(tail -n 1 $journal_path)

echo -e "\n\nPlans for today:\n\n"
echo $last_page | jq -r '.plans | to_entries | map("\(.key). \(.value)") | join("\n\n")'
echo -e "\n\n\n"
cowsay -f moose "Good luck with your chores!"
sudo sysctl -w vm.drop_caches=3 >/dev/null
