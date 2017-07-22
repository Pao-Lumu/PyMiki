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

    @commands.group(pass_context=True, aliases=['bms', 'buyslot'])
    async def buymarriageslot(self, ctx):
        # TODO 
        # Add ability to check SQL db for a given ID
        limit = 10
        e = discord.Embed()
        if ctx.invoked_subcommand is None:
            if 19 >= limit:
                e.description = "Each user can have a maximum of **{limit} marriage slots**. You have reached this cap."
                e.color = discord.Color(0xFF9966)
                await self.bot.say(embed=e)
            else:
                e.description="Would you like to buy a marriage slot?"
                e.color = discord.Color(0xFF9966)
                await self.bot.say(embed=e)

    @buymarriageslot.command(name='yes')
    async def _yes_bms(self):
        await self.bot.say("NYI")

    @commands.command(name='leaderboards', aliases=['leaderboard', 'lb'])
    async def leaderboards(self):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='divorce', aliases=['div'])
    async def divorce(self, ctx):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='profile')
    async def profile(self, ctx):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='marry')
    async def marry(self, ctx):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='declinemarriage')
    async def declinemarriage(self, ctx):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='acceptmarriage')
    async def acceptmarriage(self, ctx):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='showproposals')
    async def showproposals(self, ctx):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='rep')
    async def rep(self, ctx):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='give')
    async def give(self, ctx):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='syncavatar')
    async def syncavatar(self, ctx):
        # low priority
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='syncname')
    async def syncname(self, ctx):
        # low priority
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='setrolelevel')
    async def setrolelevel(self, ctx):
        # low priority
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='daily')
    async def daily(self, ctx):
        await self.bot.say("NYI")

    @commands.command(pass_context=True,name='moneys')
    async def moneys(self, ctx):
        await self.bot.say("NYI")

def setup(bot):
    bot.add_cog(Account(bot))

