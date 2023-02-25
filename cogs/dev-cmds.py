import imp
import disnake
from disnake.ext import commands, tasks
import os
import sys
import json
from func import *
from checks import *

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="guilds", description="Опасно секретно.")
    async def __guilds(self, ctx):
        if check_bot_owner(ctx.user.id) is True:
            embed = disnake.Embed(title=f"Список всех гильдий", description=f"{list(self.bot.guilds)}", color=disnake.Color.dark_theme())
            await ctx.send(embed=embed)
        else:
            dev = disnake.Embed(title=f"Ошибка", description=f"Данную команду может использовать только разработчики бота!", color=disnake.Color.red())
            await ctx.send(embed=dev)

    @commands.slash_command(name="load", description="Опасно секретно.")
    async def load(self, ctx, extension):
        if check_bot_owner(ctx.user.id) is True:
            self.bot.load_extension(f"cogs.{extension}")
            await ctx.send("Готово")
        else:
            dev2 = disnake.Embed(title=f"Ошибка", description=f"Данную команду может использовать только разработчики бота!", color=disnake.Color.red())
            await ctx.send(embed=dev2)

    @commands.slash_command(name="reload", description="Опасно секретно.")
    async def __reload(self, ctx, extension):
        if check_bot_owner(ctx.user.id) is True:
            self.bot.unload_extension(f"cogs.{extension}")
            self.bot.load_extension(f"cogs.{extension}")
            await ctx.send("Готово")
        else:
            devvv = disnake.Embed(title=f"Ошибка", description=f"Данную команду может использовать только разработчики бота!", color=disnake.Color.red())
            await ctx.send(embed=devvv)

    @commands.slash_command(name="unload", description="Опасно секретно.")
    async def __unload(self, ctx, extension):
        if check_bot_owner(ctx.user.id) is True:
            self.bot.unload_extension(f"cogs.{extension}")
            await ctx.send("Готово")
        else:
            devv = disnake.Embed(title=f"Ошибка", description=f"Данную команду может использовать только разработчики бота!", color=disnake.Color.red())
            await ctx.send(embed=devv)

        

def setup(bot):
    bot.add_cog(owner(bot))