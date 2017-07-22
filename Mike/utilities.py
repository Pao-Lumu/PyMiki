import discord


async def error_embed(msg):
    e = discord.Embed(color=discord.Color.red())
    # e.set_author(name=":no_entry_sign: Something went wrong!")
    e.description = msg
    return e


async def success_embed(msg):
    e = discord.Embed(color=discord.Color.green())
    e.description = msg
    return e
