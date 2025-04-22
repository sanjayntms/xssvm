#!/bin/bash
sudo apt update
sudo apt install -y python3-pip
pip3 install flask
mkdir -p /var/www/xssdemo
cp -r * /var/www/xssdemo/
nohup python3 /var/www/xssdemo/app/app.py &
