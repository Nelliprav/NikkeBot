import disnake
from disnake.ext import commands, tasks
import os
import random
import sys
from func import *
from settings import settings
from checks import *

bot = load_json("developers.json")
bot = load_json("premium.json")

bot = commands.AutoShardedBot(shard_count=5, command_prefix = settings['prefix'], intents = disnake.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status = disnake.Status.dnd, activity = disnake.Activity(name = f'/help | Гильдий: {len(bot.guilds)} | Юзеров: {len(bot.users)}', type = disnake.ActivityType.watching))
    check_blacklist.start()
    print("""
  _   _ _ _    _        ____        _   
 | \\ | (_) | _| | _____| __ )  ___ | |_ 
 |  \\| | | |/ / |/ / _ \\  _ \\ / _ \\| __|
 | |\\  | |   <|   <  __/ |_) | (_) | |_ 
 |_| \\_|_|_|\\_\\_|\\_\\___|____/ \\___/ \\__|
      """)
    print("INFO")
    print()
    print(f"NAME BOT: {bot.user.name}")
    print(f"ID BOT: {bot.user.id}")
    print(f"USERS: {len(bot.users)}")
    print(f"SERVERS: {len(bot.guilds)}")
#if check_premium(ctx.guild.id) is False:
#    else:


@tasks.loop(seconds=3)
async def check_blacklist():
    blacklist = load_json("blacklist.json")
    for guild in bot.guilds:
        if guild.id in blacklist['list']:
            embed = disnake.Embed(title='Вы в чёрном списке!', description=f'Ваш сервер {guild.name} находится в чёрном списке бота! Я покидаю вас и ваш сервер.', color=disnake.Color.red())
            await guild.owner.send(embed=embed)
            await guild.leave()

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")





bot.run(settings['token'])


