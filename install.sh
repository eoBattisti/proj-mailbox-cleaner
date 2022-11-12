#!/bin/bash
set -x
set -e

if [[ "$#" -ne 2 ]]; then
    echo "Please check the number of arguments"
    exit
fi

export EMAIL_USERNAME=$1
export EMAIL_PASSWORD=$2

if [[ `id -u` -ne 0 ]]; then
    echo "Please run the script as sudo"
    exit
fi

echo "Setting up cron jobs"
(crontab -l; echo "@reboot sleep 5 && /opt/email-cleaner/cleaner.py")|awk '!x[$0]++'|crontab -
echo "Cron jobs set up done!"
