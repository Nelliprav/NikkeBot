from importlib.metadata import requires
import disnake
from disnake.ext import commands
from checks import *
from disnake.ui import *
import aiohttp

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "1")
    async def idea(self, *, ctx):
        pass
    
    @commands.slash_command(
        name="feedback",
        description="Обращение к разработчикам.",
        options=[
            disnake.Option(
                "text",
                "Напишите текст чтобы отправить сообщение разработчикам.",
                required=True
            )
        ]
    )
    async def __feedback(self, ctx, *, text):
        channel = self.bot.get_channel(1004721817069572208)
        embed = disnake.Embed(title="Поддержка", color=disnake.Color.green())
        embed.add_field(name=f"Пользователь:", value=ctx.author.name)
        embed.add_field(name=f"Пользователь ID:", value=ctx.author.id)
        embed.add_field(name=f"Обращение:", value=text)
        embed.add_field(name=f"Гильдия:", value=ctx.guild.name)
        embed.add_field(name=f"Гильдия ID:", value=ctx.guild.id)
        embed.set_thumbnail(url=ctx.author.display_avatar)
        embed.set_footer(icon_url=ctx.guild.icon.url, text=ctx.guild.name)
        await channel.send(embed=embed)
        return await ctx.send(f"{ctx.author.mention}, Спасибо за обращение мы будем помнить вас!")


    @commands.guild_only()
    @commands.slash_command(
        name="server-info",
        description="Информация о сервере."
    )
    async def serverinfo(self, ctx):
        premium_guilds = load_json("premium.json")
        if premium_guilds[f'{ctx.guild.id}'] == "true":
            premium = "Nikke Premium преобретена на данном сервере :white_check_mark: "
        else:
            premium = "Nikke Premium не преобретена на данном сервере :x: "
        all = len(ctx.guild.members)
        members = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
        bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members))),

        ]
        embed = disnake.Embed(title=f"{ctx.guild.name}", color=disnake.Colour.dark_theme())
        embed.add_field(name="Статусы:", value=f"<:online:1004603442867748918> В сети: {statuses[0]}\n <:idle:1004603865204789318> Не активен: {statuses[1]}\n <:dnd:1004604281845977088> Не беспокоить: {statuses[2]}\n <:offline:1004661482488877118> Не в сети: {statuses[3]}", inline=False)
        embed.add_field(name="Участники:", value=f"<:all:1004659237336657972> Всего: {all}\n <:members:1004660546282475530> Людей: {members}\n <:bot:1004668108981665832> Ботов: {bots}", inline=False)
        embed.add_field(name='Дата создания сервера:', value=ctx.guild.created_at.strftime("`%b %d %Y`"), inline=False)
        embed.add_field(name='Владелец:', value=f"<@{ctx.guild.owner_id}>", inline=False)
        embed.add_field(name='Каналы:', value=f'<:channels:1004665761383579659> Текстовых: {len(ctx.guild.text_channels)}\n <:voice_channels:1004667343500230676> Голосовых: {len(ctx.guild.voice_channels)}', inline=False)
        embed.add_field(name='Подписка:', value=f'{premium}', inline=False)
        embed.set_thumbnail(url=ctx.guild.icon)  
        embed.set_footer(text=f"ID: {ctx.guild.id}")
        await ctx.response.send_message(embed=embed)


    @commands.slash_command(name="send-dm", description="Отправить кому-то в лс от имени бота")
    @commands.guild_only()
    async def send(self, ctx, member: disnake.Member, *, text):
        embed = disnake.Embed(title="Обращение к вам!", color=disnake.Color.dark_red())
        embed.add_field(name="Отправитель:", value=ctx.author.name)
        embed.add_field(name="Сообщение:", value=text)
        embed.set_thumbnail(url=ctx.author.display_avatar)
        embed.set_footer(text=f"Отправлено с: {ctx.guild.name}")
        await member.send(embed=embed)
        return await ctx.send(f"{ctx.author.mention}, Успешно отправил участнику: {member.name}")

    @commands.slash_command(description="Мемы!!!")
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/meme")
            memejson = await request.json()
            dogf = disnake.Embed(title = f"<a:pepememe:997709414297518171> Мемчик!", color = 0x38f09a)
            dogf.set_footer(text="Nikke Bot © 2022 Все права защищены")
            dogf.set_image(url=memejson['image'])
            await ctx.send(embed = dogf)

    @commands.slash_command(description="Писать от имени бота..")
    async def say(self, ctx, *, text):
        await ctx.send(text)

    @commands.slash_command(name="avatar", description="Аватар юзера")
    async def __avatar(self, ctx, *, member: disnake.Member = None):
        if member is None:
            member=ctx.author
            embed = disnake.Embed(title=f"{member.name}", color=disnake.Color.green())
            embed.set_image(url='{}'.format(member.display_avatar))
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(general(bot))