from datetime import datetime

from telethon import TelegramClient, events
from private import *

client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    print("Nick_name:", event.sender.username, ', date: ', datetime.now())
    print(event.raw_text, '\n')


client.start()
client.run_until_disconnected()
