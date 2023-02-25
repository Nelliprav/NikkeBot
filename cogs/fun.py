import disnake
import io
import os
import aiohttp
from disnake.ext import commands
from asyncio import sleep
import datetime
from random import randint, random
import requests

emails=[
    "hecker228@gmail.com",
    "a4@gmail.com",
    "fe4grtkrt9hrtjk@gmail.com",
    "allka2008@gmail.com",
    "kriper2008@gmail.com",
    "gay742@gmail.com",
    "quodufeiwappe-6289@yopmail.com",
    "ceugramohive-6944@yopmail.com",
    "joigreppefroppu-6514@yopmail.com"
    "lorikbik@omdiaco.com",
    "tillman.neal@hotmail.com",
    "q9@mail.ru",
    "3vmtdo1@outlook.com",
    "r3p4mgf5@yandex.ru",
    "qo2sc@mail.ru",
    "v9dux@gmail.com",
    "5ntglejc9@outlook.com",

]


passwords = [
    "g3rafXaW",
    "5Nhg3KwZ",
    "i2xJC7hHfAhDG9ySMfqk",
    "Gw1ZM",
    "xpm8hrvmpN4ZXUcn4gzv",
    "QyhMa7LhLMgYS4xUb3ar",
    "tW1E0WBPEM0Q3JmBJjpR",
    "oYx6oTZkYxb0YUN5ev3v",
    "t7UAuT84tFbVFki1QLQE",
    "G)rPidQdcm>2i{VA^S0d",
    "[pnG$hhWB^6{7rLv^5L&",
    "btgMr",
    "ivanzolo2004"
]

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Проверка бота")
    async def test(self, ctx):
        message = await ctx.send(f"Проверка бота.")
        await sleep(1)
        await message.edit(content="Проверка бота..")
        await message.edit(content="Проверка бота...")
        await message.edit(content="Бот в норме!")
        await message.edit(content="<:yes:992070935471468624>")

    @commands.command(name="hack2344")
    async def hack_(self, ctx, *, member: disnake.Member):
        
        message = await ctx.send(f"`C:/> Login discord Datebase`")
        await sleep(0.4)
        await message.edit(content="`[INFO]: Успешный вход в базу данных`")
        await sleep(0.4)
        await message.edit(content="`[INFO]: Ищем юзера которого вы указали...`")
        await sleep(0.4)
        await message.edit(content="`[INFO]: Юзер не найден в базе данных повторяю попытку..`")
        await sleep(0.4)
        await message.edit(content="`[INFO]: 1%`")
        await sleep(0.4)
        await message.edit(content="`[INFO]: 20%`")
        await sleep(0.4)
        await message.edit(content="`[INFO]: 90%`")
        await sleep(0.4)
        await message.edit(content="`[INFO]: 100%`")
        await sleep(0.4)
        await message.edit(content=f"`[INFO]: Юзер найден {member.name}!`")
        await sleep(0.4)
        await message.edit(content="`[INFO]: Начинаем отслеживать его по IP адресу!`")
        await sleep(0.4)
        await message.edit(content="`[INFO]: Мы его отследили сейчас скажем его IP адрес!`")
        await sleep(0.4)
        await message.edit(content=f"`[INFO]: Вот всё его данные`")
        await ctx.send(f"[INFO]: Email: {random.choice(emails)}\nПароль: {random.choice(passwords)}")
        await ctx.send("[INFO]: IP Адрес: 127.0.0.1:8080")
    

    @commands.command()
    async def login_accgdsd(self, ctx, member: disnake.Member):
        await ctx.send(f"Вхожу на аккаунт данного юзера: {member.name}")
        await ctx.send(f"**Вошёл в аккаунт**")
        await ctx.send("Начинаю сканировать данный аккаунт")
        await ctx.send(f"Отправил данные юзеру который использовал данную комаду.")
        await ctx.author.send("Вот его данные: \n**Gmail:** hecker228@gmail.com \n**Пароль:** kriper2008")


    @commands.slash_command(name="discord-nitro", description="Бесплатное discord nitro!!")
    async def dsnitro(self, ctx):
        await ctx.send("https://tenor.com/view/rick-roll-nitro-gif-21997352")

def setup(bot):
    bot.add_cog(fun(bot))