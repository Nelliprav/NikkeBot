import disnake
from disnake.ext import commands
from checks import *
from func import *
from enum import Enum


class blacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(
        name="blacklist-add",
        description="Управление чёрным списком (доступно разработчику)",
        options=[
            disnake.Option("guild", "ID Гильдии.", disnake.OptionType.string, required=True)
        ]
    )
    async def __blacklsit(self, ctx, guild: str):
        if check_bot_owner(ctx.user.id) is True:
            blacklist['list'].append(str(guild))
            write_json("blacklist.json", blacklist)
            embed = disnake.Embed(title='Готово', description=f"Данный ID гильдии был успешно занесён в чёрный список!", color=disnake.Color.green())
            await ctx.send(embed=embed)
        else:
            devv = disnake.Embed(title=f"Ошибка", description=f"Данную команду может использовать только разработчики бота!", color=disnake.Color.red())
            await ctx.send(embed=devv)

def setup(bot):
    bot.add_cog(blacklist(bot))                