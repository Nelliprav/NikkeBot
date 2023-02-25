import disnake
from disnake.ext import commands
from pymongo import MongoClient

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#        self.cluster = MongoClient("mongodb+srv://Nikke:7GAiNPxpp84bq60X@nikkedb.2przb0d.mongodb.net/?retryWrites=true&w=majority")
#        self.collection = self.cluster.ecodb.colldb

#    @commands.command(
#        name="balance",
#        aliases="bal, cash",
#        usage="balance <@user>"
#    )
#    async def user_bal(self, ctx, member: discord.Member = None):
#        if member is None:
#            await ctx.send(embed = discord.Embed(
#                description = f"Баланс юзера __{ctx.author}__: **{self.collection.find_one({'_id': ctx.author.id})['balance']}**"
#            ))
#        else:
#            await ctx.send(embed = discord.Embed(
#               description = f"Баланс юзера __{member}__: **{self.collection.find_one({'_id': ctx.member.id})['balance']}**"
#            ))


def setup(bot):
    bot.add_cog(Economy(bot))