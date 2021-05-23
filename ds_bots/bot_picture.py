import os
import config
import discord

client = discord.Client()



@client.event
async def on_ready():
    print('Бот {0.user} залогинился и котов показать котика или пёсика'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('котик'):
        cat = os.path.join(os.path.dirname(__file__), "C:/Users/kirih/PycharmProjects/discord_bot/cat.jpg")
        await message.channel.send(file=discord.File(cat))

    if message.content.startswith('песик'):
        dog = os.path.join(os.path.dirname(__file__), "C:/Users/kirih/PycharmProjects/discord_bot/dog.jpg")
        await message.channel.send(file=discord.File(dog))

client.run(config.TOKEN)
