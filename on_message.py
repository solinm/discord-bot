import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == "hello" or message.content.lower() == "hey" or message.content.lower() == "hi":
        await message.channel.send("hi!")

client.run("OTA1OTI3MzMzNzA4NDQzNjU4.YYRMkw.hLmaACAG7SQhiPc_qoVVQk_IoNU")