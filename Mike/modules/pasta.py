from datetime import date

import discord
from discord.ext import commands

import utilities
from miki_sql import PastaSQL


class Pasta:
    """Ravioli, ravioli, use the bot to spam-ioli."""

    def __init__(self, bot):
        self.bot = bot
        self.db = PastaSQL()
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
        if self.db.exists(cmd):
            pasta_msg = self.db.get(cmd)
            new_uses = int(pasta_msg[1]) + 1
            print(new_uses)
            self.db.update_uses(new_uses, cmd)
            await self.bot.say(pasta_msg[0])
            return
        else:
            e = await utilities.error_embed("That pasta doesn't exist!")
            await self.bot.say(embed=e)
            return

    @commands.command(pass_context=True, aliases=['cp'])
    async def createpasta(self, ctx, *text):
        """Make your very own pasta!"""
        if len(text) <= 1:
            e = await utilities.error_embed(
                "I couldn't find any content for this pasta, please specify what you want to make.")
            await self.bot.say(embed=e)
            return

        if self.db.exists(text[0].lower()):
            e = await utilities.error_embed("This pasta already exists! Try a different tag.")
            await self.bot.say(embed=e)
            return
        if len(text) >= 2:
            e = discord.Embed()
            args = (text[0].lower(), " ".join(text[1:]), ctx.message.author.id, date.today(), 0, 0, 0)
            self.db.add(args)
            e.description = "Successfully created new pasta `{}`!".format(text[0])
            await self.bot.say(embed=e)
            return
        await self.bot.say("If you're reading this, tell the developer he's an idiot.")
        return

    @commands.command(pass_context=True, aliases=['ip'])
    async def infopasta(self, ctx):
        """Get information about a pasta"""
        cmd = ctx.message.content.split(" ", 1)
        if len(cmd) == 1:
            e = await utilities.error_embed("**USAGE_REMINDER_HERE**")
            await self.bot.say(embed=e)
            return
        if self.db.exists(cmd[1]):
            pasta_info = self.db.get_info(cmd[1])
            e = discord.Embed(color=discord.Color.blue())
            e.set_author(name=pasta_info[0].upper())
            e.add_field(name="Created by", value="{} [{}]".format("NYI", pasta_info[2]))
            e.add_field(name="Date created", value=pasta_info[3])
            e.add_field(name="Times used", value=pasta_info[4])
            e.add_field(name="Rating", value="⬆️ {} ⬇️ {}".format(pasta_info[5], pasta_info[6]))
            await self.bot.say(embed=e)
            return
        e = await utilities.error_embed("**NOT_FOUND**")
        await self.bot.say(embed=e)
        return

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
        author_id = ctx.message.author.id

        if len(cmd) == 1:
            e = await utilities.error_embed("Please state which pasta you would like to remove.")
            await self.bot.say(embed=e)
            return
        cmd = cmd[1]
        if self.db.exists(cmd) is False:
            e = await utilities.error_embed("This pasta doesn't exist!")
            await self.bot.say(embed=e)
            return

        if self.db.pasta_owned(cmd, author_id):
            self.db.delete(cmd)
            e = await utilities.success_embed("Deleted pasta `{}`!".format(cmd))
            await self.bot.say(embed=e)
            return

        e = await utilities.error_embed("You don't own this pasta.")
        await self.bot.say(embed=e)
        return

    @commands.command(pass_context=True, aliases=['pp'])
    async def poppasta(self, ctx):
        """This command shows the most used pastas"""
        e = discord.Embed()
        pastas = self.db.popular()
        e.title = "Most popular pastas"
        for item in pastas:
            if item == pastas[0]:
                e.add_field(name="👑 " + str(item[0]), value=item[1])
            else:
                e.add_field(name=item[0], value=item[1])
        await self.bot.say(embed=e)

    @commands.command(pass_context=True, aliases=['tp'])
    async def toppasta(self, ctx):
        """This command shows the most loved pastas!"""
        e = await utilities.wip_embed()
        await self.bot.say(embed=e)

    @commands.command(pass_context=True, aliases=['mp'])
    async def mypasta(self, ctx):
        if ctx.message.mentions:
            user_id = ctx.message.mentions[0].id
            user_name = ctx.message.mentions[0].name + " doesn't"
        else:
            user_id = ctx.message.author.id
            user_name = "You don't"
        """"""
        mp = self.db.get_owned(user_id)
        # TODO: PAGIFY THIS!!!
        if len(mp) > 0:
            ap = []
            for item in mp:
                ap.append(item[0])
            ap.sort()
            e = discord.Embed()
            e.description = "`" + "` `".join(ap) + "`"
            await self.bot.say(embed=e)
            return
        e = await utilities.error_embed("Uh-oh! {} have any pastas!".format(user_name))
        await self.bot.say(embed=e)


def setup(bot):
    bot.add_cog(Pasta(bot))
    print("Loaded module pasta")


def teardown(bot):
    print("Stopping module pasta")
