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

    @commands.command(name="buymarriageslot")
    async def buymarriageslot(self, ctx):
        limit = 10

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