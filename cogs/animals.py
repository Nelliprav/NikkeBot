import disnake
from disnake.ext import commands
import aiohttp

class animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Собаки")
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/img/dog")
            dogjson = await request.json()
            dog = disnake.Embed(title = f":dog: Собака", color = 0x38f09a)
            dog.set_footer(text="Nikke Bot © 2022 Все права защищены")
            dog.set_image(url=dogjson['link'])
            await ctx.send(embed = dog)

    @commands.slash_command(description="Котики")
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/img/cat")
            catjson = await request.json()
            cat = disnake.Embed(title = f":cat: Кот", color = 0x38f09a)
            cat.set_footer(text="Nikke Bot © 2022 Все права защищены")
            cat.set_image(url=catjson['link'])
            await ctx.send(embed = cat)

    @commands.slash_command(description="Лисы")
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/img/fox")
            foxjson = await request.json()
            fox = disnake.Embed(title = f":fox: Лиса", color = 0x38f09a)
            fox.set_footer(text="Nikke Bot © 2022 Все права защищены")
            fox.set_image(url=foxjson['link'])
            await ctx.send(embed = fox)

    @commands.slash_command(description="Панды")
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/img/panda")
            foxjson = await request.json()
            fox = disnake.Embed(title = f":panda_face: Панда", color = 0x38f09a)
            fox.set_footer(text="Nikke Bot © 2022 Все права защищены")
            fox.set_image(url=foxjson['link'])
            await ctx.send(embed = fox)

    @commands.slash_command(name = "red-panda", description="Красные панды!")
    async def pandared(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://some-random-api.ml/img/red_panda")
            redpandajson = await request.json()
            redpanda = disnake.Embed(title = f":panda_face: Красная панда", color = 0x38f09a)
            redpanda.set_footer(text="Nikke Bot © 2022 Все права защищены")
            redpanda.set_image(url=redpandajson['link'])
            await ctx.send(embed = redpanda)

    @commands.slash_command(description="Бибры")
    async def birb(self, ctx):
            async with aiohttp.ClientSession() as session:
                request = await session.get("https://some-random-api.ml/img/birb")
                birbjson = await request.json()
                birb = disnake.Embed(title = f":bird: Бибр", color = 0x38f09a)
                birb.set_footer(text="Nikke Bot © 2022 Все права защищены")
                birb.set_image(url=birbjson['link'])
                await ctx.send(embed = birb)

    @commands.slash_command(description="Коалы")
    async def koala(self, ctx):
            async with aiohttp.ClientSession() as session:
                request = await session.get("https://some-random-api.ml/img/koala")
                koalajson = await request.json()
                koala = disnake.Embed(title = f":koala: Коала", color = 0x38f09a)
                koala.set_footer(text="Nikke Bot © 2022 Все права защищены")
                koala.set_image(url=koalajson['link'])
                await ctx.send(embed = koala)

def setup(bot):
    bot.add_cog(animals(bot))