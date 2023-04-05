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
# create .env file
cp .env.example .env
```

### Edit .env file

You need to edit the .env file. You can get the token from the [BotFather](https://t.me/BotFather) and the chat id from the [get_id_bot](https://t.me/get_id_bot).


### Setup

```bash
# open crontab
crontab -e
# add this line (!!! REPLACE "/your/project/path" WITH YOUR PROJECT PATH !!!)
* * * * * /your/project/path/venv/bin/python3 /your/project/path/main.py
```