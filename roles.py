import discord

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print("Ready")

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
client.run("OTA1OTI3MzMzNzA4NDQzNjU4.YYRMkw.hLmaACAG7SQhiPc_qoVVQk_IoNU")

