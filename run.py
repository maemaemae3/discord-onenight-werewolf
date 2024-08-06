from dowClient import dowClient
import discord

intents = discord.Intents.default()
intents.message_content = True  # Enable the intents you need

client = dowClient(intents=intents)

with open('./key', 'r') as f:
    key = f.read()

client.run(key[0:-1])
