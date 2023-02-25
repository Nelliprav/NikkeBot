import disnake
from disnake.ext import commands

nikkehelp=["@Nikke#5739"]

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        for i in nikkehelp:
            if i in message.content:
                embed = disnake.Embed(description=f"{message.author.name}, Чтобы узнать мой весь список введите команду `/help`", color=disnake.Color.dark_theme())
                await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(events(bot))