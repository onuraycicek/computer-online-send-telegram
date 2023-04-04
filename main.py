import os
import telegram
import asyncio
import time
import json
from dotenv import load_dotenv
load_dotenv() 

#path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(ROOT_DIR, 'cache.json')

#env
bot_token = os.environ.get('BOT_TOKEN')
chat_id = os.environ.get('CHAT_ID')

#content
new_message_template = """
Açılış: {open_time}
Son Aktif Zaman: {last_active_time}
"""

async def update_message():
        bot = telegram.Bot(token=bot_token)

        current_time = time.strftime('%H:%M')

        try:
            f = open(CACHE_PATH, "r")
            cached_data = json.loads(f.read())
        except:
             cached_data = None

        if cached_data:
            difftime = int(current_time.split(':')[1]) - int(cached_data['last_active_time'].split(':')[1]) # minute
            if difftime == 0:
                return
            
            print(difftime)
            print(cached_data['last_active_time'])
            
            check = difftime <= 2
            if check:
                open_time = cached_data['open_time']
                new_message_content = new_message_template.format(open_time=open_time, last_active_time=current_time)
                await bot.edit_message_text(chat_id=chat_id, message_id=cached_data['message_id'], text=new_message_content)
                f = open(CACHE_PATH, "w")
                write_data = {"open_time": open_time, "last_active_time": current_time, "message_id": cached_data['message_id']}
                f.write(json.dumps(write_data))
                f.close()
                return

        new_message_content = new_message_template.format(open_time=current_time, last_active_time=current_time)
        sended = await bot.send_message(chat_id=chat_id, text=new_message_content)
        f = open(CACHE_PATH, "w")
        write_data = {"open_time": current_time, "last_active_time": current_time, "message_id": sended.message_id}
        f.write(json.dumps(write_data))
        f.close()
            
asyncio.run(update_message())
