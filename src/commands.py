import discord
from discord.ext import commands as cms
from discord import app_commands as acms

from random import choice
from datetime import timedelta

import util

class Commands(cms.Cog):
    def __init__(self, bot):
        self.bot = bot

    @acms.command(name = "hello", description = "Kreativan pozdrav")
    async def hello(self, interaction: discord.Interaction):
        author = interaction.user
        chosen = util.pick_a_line_from_file("pozdravi.txt")
        await interaction.response.send_message(chosen.format(caller = author.mention))

    @cms.command(aliases = ["sazovi", "pozovi", "cstime"])
    async def call_up(self, ctx, duration):

        if not util.is_admin(ctx.author.id):
            await ctx.reply("Rezervisano za admine.")
            return

        chosen = util.pick_a_line_from_file("cspoll.txt")

        poll_content = chosen.split(":")
        poll = discord.Poll(
            question = poll_content[0],
            duration = timedelta(hours = float(duration))
        )

        poll.add_answer(text = poll_content[1])
        poll.add_answer(text = poll_content[2])

        await ctx.send(poll = poll)