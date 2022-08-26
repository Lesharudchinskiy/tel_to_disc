from telethon import TelegramClient, events


api_id = ######
api_hash = '########'
client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    print(event.raw_text)


client.start()
client.run_until_disconnected()
