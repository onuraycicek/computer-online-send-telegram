# Computer Online Send Telegram

## WHAT IS IT?
An automation project that updates when you start your computer and the active time during the period it is active.

## USAGE

### Install

```bash
# clone repo
git clone https://github.com/onuraycicek/computer-online-send-telegram
# go to project folder
cd computer-online-send-telegram
# create virtual environment
python3 -m venv venv
# activate virtual environment
source venv/bin/activate
# install requirements
pip3 install -r requirements.txt
```

### Setup

```bash
# open crontab
crontab -e
# add this line (!!! REPLACE "/your/project/path" WITH YOUR PROJECT PATH !!!)
* * * * * /your/project/path/venv/bin/python3 /your/project/path/main.py
```