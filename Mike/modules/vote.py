import discord
from discord.ext import commands

class Vote:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def vote(self, ctx):
        actual_vote = await self.bot.say("yeaaaah boiiiiiiiii")
        for emoji in ('\N{WHITE HEAVY CHECK MARK}', '\N{CROSS MARK}'):
            await self.bot.add_reaction(actual_vote, emoji)


def setup(bot):
    bot.add_cog(Vote(bot))
