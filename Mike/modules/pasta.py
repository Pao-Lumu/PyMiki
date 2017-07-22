import sqlite3
from datetime import date

import discord
from discord.ext import commands

import utilities


class Pasta:
    """Ravioli, ravioli, use the bot to spam-ioli."""
    def __init__(self, bot):
        self.bot = bot
        self.db = sqlite3.connect("pymiki.db")
        self.cursor = self.db.cursor()

    # pasta : (pasta_tag text, pasta_text text, creator_id text, creation_date text, uses integer, likes integer, dislikes integer)

    @commands.command(pass_context=True)
    async def pasta(self, ctx):
        """Call up a user-submitted pasta"""
        cmd = ctx.message.content.split(" ", 1)
        if len(cmd) == 1:
            e = await utilities.error_embed("Please state which pasta you would like to identify.")
            await self.bot.say(embed=e)
            return
        self.cursor.execute('''SELECT pasta_text FROM pasta WHERE pasta_tag=?''', (cmd[1],))
        pasta_msg = self.cursor.fetchone()
        print(pasta_msg)
        if pasta_msg == (0,):
            e = await utilities.error_embed("That pasta doesn't exist!")
            await self.bot.say(embed=e)
            return
        await self.bot.say(pasta_msg[0])
        return

    @commands.command(pass_context=True, aliases=['cp'])
    async def createpasta(self, ctx):
        """Make your very own pasta!"""
        e = discord.Embed()
        cmd = ctx.message.content.split(" ", 2)
        if len(cmd) <= 2:
            e = await utilities.error_embed(
                "I couldn't find any content for this pasta, please specify what you want to make.")
            await self.bot.say(embed=e)
            return
        self.cursor.execute('''SELECT * FROM pasta WHERE pasta_tag=?''', (cmd[1],))
        if self.cursor.fetchone() == (0,):
            e = await utilities.error_embed("This pasta already exists! Try a different tag.")
            await self.bot.say(embed=e)
            return
        if len(cmd) == 3:
            args = (cmd[1], cmd[2], ctx.message.author.id, date.today(), 0, 0, 0)
            self.cursor.execute('''INSERT INTO pasta VALUES (?,?,?,?,?,?,?)''', args)
            self.db.commit()
            e.description = "Successfully created new pasta `{}`!".format(cmd[1])
            await self.bot.say(embed=e)
        return

    @commands.command(pass_context=True, aliases=['ip'])
    async def infopasta(self, ctx):
        """Get information about a pasta"""
        cmd = ctx.message.content.split(" ", 1)
        if len(cmd) == 1:
            e = await utilities.error_embed("**USAGE_REMINDER_HERE**")
            await self.bot.say(embed=e)
            return
        self.cursor.execute('''SELECT * FROM pasta WHERE pasta_tag=?''', (cmd[1],))
        pasta_info = self.cursor.fetchone()
        if self.cursor.fetchone() == (0,):
            e = await utilities.error_embed("**NOT_FOUND**")
            await self.bot.say(embed=e)
            return
        e = discord.Embed(color=discord.Color.blue())
        e.set_author(name=pasta_info[0].upper())
        e.add_field(name="Created by", value="{} [{}]".format("NYI", pasta_info[2]))
        e.add_field(name="Date created", value=pasta_info[3])
        e.add_field(name="Times used", value=pasta_info[4])
        e.add_field(name="Rating", value="⬆️ {} ⬇️ {}".format(pasta_info[5], pasta_info[6]))
        await self.bot.say(embed=e)

    @commands.command(pass_context=True, aliases=['lp'])
    async def lovepasta(self, ctx):
        """Show your love for a pasta."""
        await self.vote_pasta(ctx, True)

    @commands.command(pass_context=True, aliases=['hp'])
    async def hatepasta(self, ctx):
        """Hate on a pasta. You monster."""
        await self.vote_pasta(ctx, False)

    async def vote_pasta(self, ctx, vote):
        await self.bot.say("WIP")




def setup(bot):
    bot.add_cog(Pasta(bot))
