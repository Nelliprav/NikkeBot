import disnake
from disnake.ext import commands
from disnake.ui import *
from random import randint

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(
        name="iq",
        description="Ваш IQ!"
    )
    async def __iq(self, ctx):
        randcihlo = randint(0,250)
        embed = disnake.Embed(description="Ваш IQ: {}".format(randcihlo))
        embed.set_footer(text = f"Вызвал команду: {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.slash_command(description="Узнайте на сколько вы гей!")
    async def gay(self, ctx):
        randcihlo = randint(0,100)
        kak = disnake.Embed(title = "Вы гей на {}%".format(randcihlo), description = f"{ctx.author.name} Поздравляю вы стали геим как вы ввёли эту команду и стали клубом `ЛГБТ`")
        kak.set_image(url = "https://flagof.ru/wp-content/uploads/2018/10/lgbt.png")
        kak.set_thumbnail(url = "https://img.apkgit.com/3c/com.aramvirabyan.gaytest/1.2.4/icon.png")
        await ctx.send(embed = kak)

    @commands.slash_command(description="Узнайте на сколько вы натурал!")
    async def natural(self, ctx):
        randcihlo = randint(0,5)
        kak = disnake.Embed(title = "Вы натурал на {}%".format(randcihlo))
        await ctx.send(embed = kak)


def setup(bot):
    bot.add_cog(games(bot))