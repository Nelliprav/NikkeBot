import json
import disnake
import datetime
from random import randint
from disnake.ext import commands
from func import *

bot = load_json("global_chat.json")


class GlobalChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "global-set")
    @commands.has_permissions(administrator=True)
    async def global_set(self, ctx, channel):
        guild_id = ctx.message.guild.id
        channel_id = int(channel.strip('<>#'))

        with open('global_chat.json', 'r') as file:
            global_chat_data = json.load(file)
            new_global_chat = str(guild_id)

            if new_global_chat in global_chat_data:
                await ctx.send('<a:no:997705009519140915> **Канал уже добавлен в глобальный чат!**')

            else:
                global_chat_data[new_global_chat] = channel_id
                with open('global_chat.json', 'w') as new_global_chat:
                    json.dump(global_chat_data, new_global_chat, indent=4)

                await ctx.send('<a:yes:997704849825222803> **Канал добавлен в глобальный чат!**')

    @commands.command(name = "global-remove")
    @commands.has_permissions(administrator=True)
    async def glo(self, ctx):
        guild_id = ctx.message.guild.id

        with open('global_chat.json', 'r') as file:
            global_chat_data = json.load(file)

        global_chat_data.pop(str(guild_id))

        with open('global_chat.json', 'w') as update_global_chat_file:
            json.dump(global_chat_data, update_global_chat_file, indent=4)

        await ctx.send('<a:yes:997704849825222803> **Канал удален из глобального чата!**')

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if not message.content.startswith('!'):
                with open('global_chat.json', 'r') as file:
                    global_chat_data = json.load(file)

                channel_id = list(global_chat_data.values())

                if message.channel.id in channel_id:

                    if not message.content:
                        return

                    for ids in channel_id:
                        if message.channel.id != ids:
                            embed = disnake.Embed(colour=randint(0, 0xffffff))
                            if message.attachments:
                                embed.set_image(message.attachments[0].url)
                            embed.timestamp = datetime.datetime.utcnow()
                            embed.set_author(icon_url=message.author.display_avatar, name=f'{message.author} ({message.author.id})')
                            embed.description = f'{message.content}'
                            embed.set_footer(icon_url=message.guild.icon.url, text=message.guild.name)
                            await self.bot.get_channel(ids).send(embed=embed)


    @global_set.error
    async def global_set_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            eror = disnake.Embed(colour=randint(0, 0xffffff))
            eror.timestamp = datetime.datetime.utcnow()
            eror.set_thumbnail(url = "https://cdn0.iconfinder.com/data/icons/shift-free/32/Error-512.png")
            eror.add_field(name = "**Ошибка:**", value = f"{ctx.author.name}, `Вы не указали канал для глобального чата пример: n.global-set <#канал>`")
            await ctx.send(embed = eror)
        
        if isinstance(error, commands.MissingPermissions):
            xa = disnake.Embed(title = f"<a:no:997705009519140915> Ошибка...", description = "У вас нет нужных прав.", color = 0xe24646)
            await ctx.send(embed=xa)

    
    @glo.error
    async def glo_handler(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            glo = disnake.Embed(title = f"<a:no:997705009519140915> Ошибка...", description = "У вас нет нужных прав.", color = 0xe24646)
            await ctx.send(embed=glo)

def setup(bot):
    bot.add_cog(GlobalChat(bot))