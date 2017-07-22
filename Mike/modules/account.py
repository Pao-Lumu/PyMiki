from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
import io

class Account:
    """"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def buymarriageslot(self,ctx):
        # TODO 
        # Add ability to check SQL db for a given ID
        limit = 10
        e = discord.Embed()
        print(type(ctx.message.channel))
        if 19 >= limit:
            e.description = "Each user can have a maximum of **{limit} marriage slots**. You have reached this cap."
            e.color = discord.Color(0xFF9966)
            await self.bot.say(embed=e)
        else:
            e.description="NANI???"
            # embed.color = discord.Color((255, 153, 102))
            await self.bot.say(embed=e)

    @buymarriageslot.command(name='yes')
    async def _yes_bms(self):
        await self.bot.say("sure")

    @commands.command(name='leaderboards', aliases=['leaderboard', 'lb'])
    async def leaderboards(self, ctx):
        return

    @commands.command(name='divorce', aliases=['div'])
    async def divorce(self, ctx):
        return

    @commands.command(name='profile')
    async def profile(self, ctx):
        return

    @commands.command(name='marry')
    async def marry(self, ctx):
        return

    @commands.command(name='declinemarriage')
    async def declinemarriage(self, ctx):
        return

    @commands.command(name='acceptmarriage')
    async def acceptmarriage(self, ctx):
        return

    @commands.command(name='showproposals')
    async def showproposals(self, ctx):
        return

    @commands.command(name='rep')
    async def rep(self, ctx):
        return

    @commands.command(name='give')
    async def give(self, ctx):
        return

    @commands.command(name='syncavatar')
    async def syncavatar(self, ctx):
        return

    @commands.command(name='syncname')
    async def syncname(self, ctx):
        return

    @commands.command(name='setrolelevel')
    async def setrolelevel(self, ctx):
        return

    @commands.command(name='daily')
    async def daily(self, ctx):
        return

    @commands.command(name='moneys')
    async def moneys(self, ctx):
        return

def setup(bot):
    print(type(bot))
    bot.add_cog(Account(bot))

