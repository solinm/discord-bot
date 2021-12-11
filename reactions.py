import discord

client = discord.Client()

@client.event
async def on_ready():
    print("online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "awesome":
        await message.add_reaction("\U0001F914")
    elif message.content == "lol":
        await message.add_reaction("\U0001F923")

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edited a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

client.run("OTA1OTI3MzMzNzA4NDQzNjU4.YYRMkw.hLmaACAG7SQhiPc_qoVVQk_IoNU")
