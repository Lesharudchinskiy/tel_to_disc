import discord
from private import TOKEN

client = discord.Client()


class Disc():

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def resend_message(message):
        channel.send('SOMETHING')

    client.run(TOKEN)


Disc()