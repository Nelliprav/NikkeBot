import disnake
from disnake.ext import commands
import datetime
from random import randint

class information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Поддержка бота")
    async def support(self, ctx):
        await ctx.send("Вот держи брат: https://discord.gg/UhTeX8uFX6")


    @commands.slash_command(description="Информация о Nikke")
    async def bot(self, ctx):
        info=disnake.Embed(title = "<a:dsbot:997691264097075342> Информация о боте", description = f"Информация об **Nikke**", colour=randint(0, 0xffffff))
        info.add_field(name = "<:dev:992151726880727151> Разработчики:", value = "`Nelli#8250, Vitness#5633 (помогает с ошибками)`")
        info.add_field(name = "<:discordpy:997708438417199144> Моя библиотека:", value="Disnake", inline=False)
        info.add_field(name = ":floppy_disk: Моя версия:", value = "`v1.1.1`", inline=False)
        info.set_thumbnail(url="https://cdn.discordapp.com/avatars/991800308168659014/ffecdc3426c335f1d4f11427bae35622.webp?size=1024")
        info.add_field(name = "🔗 Приглашение:", value = f"[Нажми](https://discord.com/api/oauth2/authorize?client_id=991800308168659014&permissions=8&scope=bot%20applications.commands)", inline = True)
        info.add_field(name = "✨ Поддержка:", value = "[Нажми](https://discord.gg/UhTeX8uFX6)")
        info.add_field(name = "⚙️ Команд:", value = f"{len(self.bot.slash_commands)}")
        info.add_field(name = "📊 Кол-во гильдий:", value = f"{len(self.bot.guilds)}")
        info.add_field(name = ":busts_in_silhouette: Пользователей:", value = f"{len(self.bot.users)}", inline=False)
        info.add_field(name = "<:github:998241809492885506> Github:", value = "[Нажми](https://github.com/Nelliprav)", inline=False)
        info.add_field(name = "<:you:997691675168223304> Цель на YouTube канале:", value = "4/10", inline=False)
        info.add_field(name=":ping_pong: Ping:", value=f"{round(self.bot.latency * 1000)}ms")
        info.set_thumbnail(url="https://cdn.discordapp.com/avatars/991800308168659014/f4d51e01494dff47ebbfad0443afc723.webp?size=96")
        info.set_footer(text="Nikke Bot © 2022 Все права защищены")
        await ctx.send(embed=info)

    @commands.slash_command(description="Пригласить бота на свой любимый сервер!")
    async def invite(self, ctx):
        await ctx.send(f"Вот держи брат: https://discord.com/api/oauth2/authorize?client_id=991800308168659014&permissions=8&scope=bot%20applications.commands")

    @commands.slash_command(description="Новости / обновление бота")
    async def news(self, ctx):
        news = disnake.Embed(title = "<a:newsbot:997704927394664468> Новости бота.", color = 0x6df73b)
        news.add_field(name="**NIKKE v.1.1.1**", value="```py\n1. Всё команда изменены на сэлш команды \ \n2. Добавлена premium система\n3. NSFW\n```")
        news.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = news)

    @commands.slash_command(name="youtube-channel", description="Нал ютуб канал")
    async def youtubechannel(self, ctx):
        await ctx.send("Наш ютуб канал подпишись не пожалеешь\nСкоро..")


    @commands.slash_command(description="Задонатить")
    async def donate(self, ctx):
        donate = disnake.Embed(title = ":love_letter: Задонить разработчику", description = "Способ доната:\nКарта UA: 4131 2196 4705 5932\nQIWI: BIYUK")
        await ctx.send(embed = donate)

    @commands.slash_command(name = "top-guilds", description="топы сервера с большым кол-во участником")
    async def top(self, ctx):
        top = disnake.Embed(title = "Топ гильдии", description = "1 | **-**\n2 | **-**\n3 | **-**\n4 | **-**\n 5 | **-**")
        await ctx.send(embed = top)

    @commands.slash_command(description="Информация о premium")
    async def premium(self, ctx):
        embed = disnake.Embed(title=f"Nikke Premium | {ctx.guild.name}", description="Преимущество:\n- Доступ к VIP серверу я там отвечаю на вопросы\n- Вы получите роль `Premium` на официальном сервере бота\n- Доступ к Premium командам.\n- Станите лучшим\n\nЧтобы купить подписку пропишите: `n.buy-premium`", color=disnake.Color.dark_theme())
        await ctx.send(embed=embed)

    @commands.slash_command(name="buy-premium", description="Купить premium подписку.")
    async def buypremium(self, ctx):
        embed = disnake.Embed(title="Покупка подписки.", description=f"Реквизиты:\nКарта UA: 4131219647055932\n[DonationAlerts](https://www.donationalerts.com/r/nastya__0561)\n\nЗаявка: \n1) ID сервера\n2) Ник в дс пример: User#0000\n- [Discord Сервер](https://discord.gg/UhTeX8uFX6)\n\n`Если вы всё оплатили зайдите на сервер и напишите в канал #『💲』получение-подписки ( по форме )`", color=disnake.Color.blurple())
        embed.set_author(name=f"{ctx.author.name}")
        await ctx.author.send(embed=embed)
        return await ctx.send(f"{ctx.author.mention}, Проверьте свои личные сообщение.")

def setup(bot):
    bot.add_cog(information(bot))