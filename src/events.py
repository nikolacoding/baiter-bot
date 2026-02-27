import discord
from discord.ext import commands as cms
from discord import app_commands as acms

import constants

class Events(cms.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cms.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        
        # dict formata {sadrzaj : reakcija}
        # za prevenciju stekovanja, dodati return na prvi prolaz petlje
        for content, reaction in constants.content_reactions.items(): 
            if content.lower() in ctx.content.lower():
                await ctx.add_reaction(reaction)