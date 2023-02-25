import disnake
from disnake.ext import commands
import datetime

class nikkedev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role("🗂️ • Следящий за анкетами")
    async def accept(self, ctx, member: disnake.Member):
        await ctx.channel.purge(limit = 1)
        await ctx.send(f"{member.mention} посмотрите сообщение!")
        embed = disnake.Embed(
            title = "Важное обращение!",
            description = f"{member.name}, Вам одобрили анкету сейчас вам выдадут роль ожидайте!",
            color = 0x2ff976
        )
        await ctx.send(embed=embed)


    @accept.error
    async def accept_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            feedd = disnake.Embed(title = f"<:No:992074530828853299> Ошибка...", description = "Вы не указали аргумент.", color = 0xe24646)
            await ctx.send(embed = feedd)

        if isinstance(error, commands.MissingRole):
            role = disnake.Embed(
                title = "<:No:992074530828853299> Ошибка...",
                description = "Возможно у вас нет роли <@&996739444797354014>",
                color = 0xe24646
            )
            await ctx.send(embed=role)

    
    @commands.command(name = "dis-accept")
    @commands.has_role("🗂️ • Следящий за анкетами")
    async def disaccept(self, ctx, member: disnake.Member):
        await ctx.channel.purge(limit = 1)
        dis = disnake.Embed(
            title = ":x: Отказано",
            description = f"{member.name}, Вам отказли анкету исправьте её или приходите в следующий раз.",
            color = 0xd64343
        )
        await ctx.send(embed=dis)

    @disaccept.error
    async def disaccept_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            d = disnake.Embed(title = f"<:No:992074530828853299> Ошибка...", description = "Вы не указали аргумент.", color = 0xe24646)
            await ctx.send(embed = d)

        if isinstance(error, commands.MissingRole):
            disaccept = disnake.Embed(
                title = "<:No:992074530828853299> Ошибка...",
                description = "Возможно у вас нет роли <@&996739444797354014>",
                color = 0xe24646
            )
            await ctx.send(embed=disaccept)

    @commands.command(name = "help-dev")
    @commands.has_role("🗂️ • Следящий за анкетами")
    async def helpdev(self, ctx):
        await ctx.channel.purge(limit = 1)
        helpdev = disnake.Embed(
            title = f"{ctx.guild.name}",
            description = "`n.accept - Принят участника в команду разработчиков,` `dis-accept - Отключить анкету.`",
            color = 0xe24646
        )
        await ctx.send(embed=helpdev)

    @helpdev.error
    async def helpdev_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            helpm = disnake.Embed(
                title = "<:No:992074530828853299> Ошибка...",
                description = "Возможно у вас нет роли <@&996739444797354014>",
                color = 0xe24646
            )
            await ctx.send(embed=helpm)

def setup(bot):
    bot.add_cog(nikkedev(bot))