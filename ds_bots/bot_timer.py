from datetime import datetime
import time
from discord.ext import commands

import config

bot = commands.Bot(command_prefix="!")




@bot.command()
async def timer(ctx):
    print("до вайла работаю")
    while True:
        print("после вайла работаю")
        time_now = datetime.now().time()
        await ctx.send("время "+str(time_now.hour)+":"+str(time_now.minute)+" наступило")
        time.sleep(60)


bot.run(config.TOKEN)
