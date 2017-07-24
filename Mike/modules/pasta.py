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
        # self.cursor.execute('''CREATE TABLE pasta
        # (pasta_tag text, pasta_text text, creator_id text, creation_date text,
        # uses integer, likes integer, dislikes integer)''')

    @commands.command()
    async def pasta(self, *cmd):
        """Call up a user-submitted pasta"""
        if len(cmd) == 0:
            e = await utilities.error_embed("Please state which pasta you would like to identify.")
            await self.bot.say(embed=e)
            return
        cmd = ' '.join(cmd)
        self.cursor.execute('''SELECT pasta_text,uses FROM pasta WHERE pasta_tag=?''', (cmd,))
        pasta_msg = self.cursor.fetchone()
        if pasta_msg is None:
            e = await utilities.error_embed("That pasta doesn't exist!")
            await self.bot.say(embed=e)
            return
        self.cursor.execute('''UPDATE pasta SET uses=? WHERE pasta_tag=?''', (int(pasta_msg[1]) + 1, cmd[1]))
        self.db.commit()
        await self.bot.say(pasta_msg[0])
        return

    @commands.command(pass_context=True, aliases=['cp'])
    async def createpasta(self, ctx, *text):
        """Make your very own pasta!"""
        e = discord.Embed()
        print(text)
        if len(text) <= 1:
            e = await utilities.error_embed(
                "I couldn't find any content for this pasta, please specify what you want to make.")
            await self.bot.say(embed=e)
            return
        self.cursor.execute('''SELECT * FROM pasta WHERE pasta_tag=?''', (text[0].lower(),))
        if self.cursor.fetchone() is not None:
            e = await utilities.error_embed("This pasta already exists! Try a different tag.")
            await self.bot.say(embed=e)
            return
        if len(text) >= 2:
            args = (text[0].lower(), " ".join(text[1:]), ctx.message.author.id, date.today(), 0, 0, 0)
            self.cursor.execute('''INSERT INTO pasta VALUES (?,?,?,?,?,?,?)''', args)
            self.db.commit()
            e.description = "Successfully created new pasta `{}`!".format(text[0])
            await self.bot.say(embed=e)
            return
        await self.bot.say("If you're reading this, tell the developer.")
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
        e = await utilities.wip_embed()
        await self.bot.say(embed=e)

    @commands.command(pass_context=True, aliases=['dp'])
    async def deletepasta(self, ctx):
        """Remove a pasta. Accidents happen."""
        cmd = ctx.message.content.split(" ", 1)
        if len(cmd) == 1:
            e = await utilities.error_embed("Please state which pasta you would like to remove.")
            await self.bot.say(embed=e)
            return
        self.cursor.execute('''SELECT * FROM pasta WHERE pasta_tag=? AND creator_id=?''',
                            (cmd[1], ctx.message.author.id))
        if self.cursor.fetchone() == (0,):
            e = await utilities.error_embed("You either don't own this pasta or it doesn't exist.")
            await self.bot.say(embed=e)
            return
        self.cursor.execute('''DELETE FROM pasta WHERE pasta_tag=? AND creator_id=?''', (cmd[1], ctx.message.author.id))
        self.db.commit()
        e = await utilities.success_embed("Deleted pasta `{}`!".format(cmd[1]))
        await self.bot.say(embed=e)
        return

    @commands.command(pass_context=True, aliases=['pp'])
    async def poppasta(self, ctx):
        """This command shows the most used pastas"""
        e = discord.Embed()
        self.cursor.execute(''''SELECT * FROM pasta ORDER BY uses DESC LIMIT 12''')
        pastas = self.cursor.fetchall()
        e.title = "Most popular pastas"
        for item in pastas:
            if item == pastas[0]:
                e.add_field(name="👑 " + str(item[0]), value=item[4])
            else:
                e.add_field(name=item[0], value=item[4])
        await self.bot.say(embed=e)

    @commands.command(pass_context=True, aliases=['tp'])
    async def toppasta(self, ctx):
        """This command shows the most loved pastas!"""
        e = await utilities.wip_embed()
        await self.bot.say(embed=e)

    @commands.command(pass_context=True, aliases=['mp'])
    async def mypasta(self, ctx):
        authorid = ""
        if ctx.message.mentions:
            authorid = ctx.message.mentions[0].id
        else:
            authorid = ctx.message.author.id
        """"""
        self.cursor.execute('''SELECT pasta_tag FROM pasta WHERE creator_id=?''', (authorid,))
        mp = self.cursor.fetchall()
        if len(mp) >= 1:
            ap = []
            for item in mp:
                ap.append(item[0])
            ap.sort()
            e = discord.Embed()
            e.description = "`" + "` `".join(ap) + "`"
            await self.bot.say(embed=e)
            return
        e = await utilities.error_embed("Uh-oh! " + ctx.message.mentions[0].name + " doesn't have any pastas!")
        await self.bot.say(embed=e)


def setup(bot):
    bot.add_cog(Pasta(bot))
    print("Loaded module pasta")


def teardown(bot):
    print("Stopping module pasta")
