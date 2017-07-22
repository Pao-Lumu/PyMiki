from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
import io
import sqlite3

class Pasta:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def pasta(self, ctx):
        self.bot.say("PASTA IS WIP")
        return


def setup(bot):
    bot.add_cog(Pasta(bot))

