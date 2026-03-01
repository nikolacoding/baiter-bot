import discord
from discord.ext import commands as cms
from discord import app_commands as acms

import constants
import util

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
                print(f"reakcija: {reaction}")
                await ctx.add_reaction(reaction)

    @cms.Cog.listener()
    async def on_presence_update(self, before, after):
        user_id = before.id
        user = await self.bot.fetch_user(user_id)
        if util.is_privileged_user(user_id) and before.activities != after.activities:
            for activity in after.activities:
                if activity and activity.type == discord.ActivityType.playing:
                    # (ako je u igrici)
                    log_channel = await self.bot.fetch_channel(constants.channel_ids["activity_log"])
                    debug_prefix = ""

                    if user and util.is_forbidden_activity(activity.name):
                        debug_prefix = "[!] "
                        choice = util.pick_a_line_from_file("forbidden_activity_reactions.txt")
                        await user.send(choice)
            
                    await log_channel.send(f"{debug_prefix}{after.display_name} sada igra '{activity.name}'")

