import disnake
from disnake.ext import commands
import datetime
from random import randint, random

class moder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.slash_command(
        description="Голосование",
        options=[
            disnake.Option("text", "Введите текст!", required=True)
        ]
    )
    @commands.has_permissions(administrator = True)
    async def poll(self, ctx, *, text):
        await ctx.channel.purge(limit = 1)
        poll = disnake.Embed(description = text, colour=randint(0, 0xffffff))
        poll.timestamp = datetime.datetime.utcnow()
        msg = await ctx.channel.send(embed = poll)
        await msg.add_reaction("✔")
        await msg.add_reaction("❌")

    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.slash_command(
        name = 'clear',
        description = 'Очистка чата',
    options = [
    disnake.Option("amount", "Кол-во сообщений, которое нужно удалить", disnake.OptionType.integer, required=True)
  ]
)
    async def clear(self, inter, amount: int):
        if amount > 500:
            embed = disnake.Embed(title=f'Ошибка', description='Вы не можете удалить более 500-cта сообщений разом!', color=disnake.Color.red())
            await inter.response.send_message(embed=embed)
        else:
            embed = disnake.Embed(title='Идёт удаление...', description=f'Идёт удаление {amount} сообщений(-я, -e)! Подождите пожалуйста чуть-чуть...')
            await inter.response.send_message(embed=embed)
            await inter.channel.purge(limit=amount)
            embed = disnake.Embed(title='Готово', description=f'Я успешно смог очистить в этом канале {amount} сообщений(-я, -е)! <:yes2:997939807580416700>', color=disnake.Color.green())
            await inter.channel.send(embed=embed)


    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            error = disnake.Embed(title = f"<:No:992074530828853299> Ошибка...", description = "Вы не указали аргумент.", color = 0xe24646)
            await ctx.send(embed = error)
        if isinstance(error, commands.MissingPermissions):
            errorr = disnake.Embed(title = f"<:No:992074530828853299> Ошибка...", description = "У вас нет нужных прав.", color = 0xe24646)
            await ctx.send(embed = errorr)

    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            er = disnake.Embed(title = f"<:No:992074530828853299> Ошибка...", description = "Вы не указали аргумент.", color = 0xe24646)
            await ctx.send(embed = er)
        
        if isinstance(error, commands.MissingPermissions):
            m = disnake.Embed(title = f"<:No:992074530828853299> Ошибка...", description = "У вас нет нужных прав.", color = 0xe24646)
            await ctx.send(embed = m)

    @commands.slash_command(
        description="Текст из эмодзи как у Dank Memer",
        options=[
            disnake.Option("text", "Введите текст на англ.", required=True)
        ]
    )
    async def emojify(self, ctx, *, text):
        emojis = []
        for s in text.lower():
            if s.isdecimal():
                num2emo = {'0':'zero' ,'1':'one', '2':'two',
                            '3':'three', '4':'four', '5':'five',
                            '6':'six', '7':'seven', '8':'eight', '9':'nine'}
                emojis.append(f':{num2emo.get(s)}:')
            elif s.isalpha():
                emojis.append(f':regional_indicator_{s}:')
            else:
                emojis.append(s)
        await ctx.send(' '.join(emojis))


    @emojify.error
    async def emojify_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            feedd = disnake.Embed(title = f"<:No:992074530828853299> Ошибка...", description = "Вы не указали аргумент.", color = 0xe24646)
            await ctx.send(embed = feedd)
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def setnick(self, ctx, member: disnake.Member, *, nick):
        setnick = disnake.Embed(title = "Информация:", color=0x00ff00)
        setnick.add_field(name = "Новый ник:", value = f"{nick}")
        setnick.add_field(name = f"Участник:", value = f"{member.mention}")
        setnick.add_field(name = "Запросил:", value = f"{ctx.author.mention}")
        setnick.set_thumbnail(url = member.avatar_url)
        setnick.set_footer(text = "Успех!")
        await member.edit(nick=nick)
        await ctx.send(embed = setnick)

    @commands.slash_command(description="Скоро..")
    async def idea(self, ctx):
        await ctx.send("Эй зачем ты ввёл эту команду!? она всё равно не добавлена..")


    @commands.slash_command(
        description="Эмбед",
        options=[
            disnake.Option("text", "Введите текст", required=True)
        ]
    )
    @commands.has_permissions(administrator = True)
    async def embed(self, ctx, *, text):
        await ctx.channel.purge(limit = 1)
        embed = disnake.Embed(description = text, colour=randint(0, 0xffffff))
        embed.set_footer(text="Nikke Bot © 2022 Все права защищены")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = embed)

    @embed.error
    async def embed_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            errore = disnake.Embed(title = f"<a:no:997705009519140915> Ошибка...", description = "Вы не указали аргумент.", color = 0xe24646)
            await ctx.send(embed = errore)

        if isinstance(error, commands.MissingPermissions):
            er = disnake.Embed(title = f"<a:no:997705009519140915> Ошибка...", description = "У вас нет нужных прав.", color = 0xe24646)
            await ctx.send(embed = er)

    @setnick.error
    async def setnick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            ivanzolo = disnake.Embed(title = f"<a:no:997705009519140915> Ошибка...", description = "Вы не указали аргумент.", color = 0xe24646)
            await ctx.send(embed = ivanzolo)

        if isinstance(error, commands.MissingPermissions):
            ivanzolo2004 = disnake.Embed(title = f"<a:no:997705009519140915> Ошибка...", description = "У вас нет нужных прав.", color = 0xe24646)
            await ctx.send(embed = ivanzolo2004)



def setup(bot):
    bot.add_cog(moder(bot))