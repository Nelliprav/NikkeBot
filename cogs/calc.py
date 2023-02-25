import disnake
from disnake.ext import commands

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx):
        pass

def setup(bot):
    pass