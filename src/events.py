import discord
from discord.ext import commands as cms
from discord import app_commands as acms

class Events(cms.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cms.Cog.listener()
    async def on_message(self, ctx):

        if ctx.author == self.bot.user:
            return
        
        if "burek" in ctx.content.lower():
            await ctx.add_reaction("🤓")
            return