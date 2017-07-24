import discord
from discord.ext import commands


class Reactions:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def confused(self):
        e = discord.Embed()
        await self.bot.say(embed=e)

    @commands.command()
    async def lewd(self):
        e = discord.Embed()
        await self.bot.say(embed=e)

    @commands.command()
    async def smug(self):
        e = discord.Embed()
        await self.bot.say(embed=e)

    @commands.command()
    async def pout(self):
        e = discord.Embed()
        await self.bot.say(embed=e)


def start(bot):
    bot.add_cog(Reactions(bot))
