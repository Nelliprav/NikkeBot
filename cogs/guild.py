import disnake
from disnake.ext import commands
from func import *
import shutil
from checks import *
import os

class guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = await guild.create_text_channel("nikkebot-инфо")
        await channel.set_permissions(guild.default_role, send_messages=False)
        await channel.set_permissions(guild.default_role, view_channel=False)
        path = f"guilds/{guild.id}"
        os.mkdir(path)
        shutil.copy('samples/guild_config.json', f'guilds/{guild.id}/config.json')
        shutil.copy('samples/guild_users.json', f'guilds/{guild.id}/users.json')
        shutil.copy('samples/guild_warns.json', f'guilds/{guild.id}/warns.json')
        premium_guilds = load_json("premium.json")
        premium_guilds[f'{guild.id}'] = "false"
        write_json("premium.json", premium_guilds)

        embed = disnake.Embed(title=f"Идёт настройка...", description=f"Сейчас мы заносим пользователей в базу данных ожидайте мы вам сообщим когда закончим!",color=disnake.Color.dark_theme())
        message = await channel.send(embed=embed)

        for member in guild.members:
            users = load_json(f"guilds/{guild.id}/users.json")
            users[str(member.id)] = "user"
            write_json(f"guilds/{guild.id}/users.json", users)

            embed = disnake.Embed(title=f"Настройка завершена!", description=f"Вам осталось настроить бота через слэш-команды и начать им пользоваться!", color=disnake.Color.green())
            embed.add_field(name="**Добро пожаловать**", value="**Nikke, Рад вас видить спасибо что вы добавили именно нас!** чтобы узнать список команд пропишите: `/help`\n\nЧтобы купить подписку `Nikke Premium` нужно зайти на сервер и написать разрабу: [тык](https://discord.gg/UhTeX8uFX6) ник разраба `Nelli#8250`")
            await message.edit(embed=embed)

    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            shutil.rmtree(f'guilds/{guild.id}')
        except:
            pass

    async def on_guild_channel_create(self, channel):
        try:
            config = load_json(f"guilds/{channel.guild.id}/config.json")
            if config['role'] != "none":
                role = channel.guild.get_role(int(config['role']))
                await channel.set_permissions(channel.guild.default_role, view_channel=False)
                await channel.set_permissions(role, view_channel=True)
        except KeyError:
            pass        


def setup(bot):
    bot.add_cog(guild(bot))