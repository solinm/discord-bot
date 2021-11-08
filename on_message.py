import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "hello" or message.content == "hey" or message.content == "hi":
        await message.channel.send("Hi!")

client.run("OTA1OTI3MzMzNzA4NDQzNjU4.YYRMkw.hLmaACAG7SQhiPc_qoVVQk_IoNU")
