import discord
from discord.ext import commands as cms
from commands import Commands
from events import Events

class Client(cms.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(command_prefix = "!", intents = intents)

    async def setup_hook(self):
        await self.add_cog(Commands(self))
        await self.add_cog(Events(self))
        await self.tree.sync()

    async def on_ready(self):
        print(f"Bot je onlajn kao {self.user}.")

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents = intents)

# UPOZORENJE: Token citamo iz token.txt koji MORA biti u .gitignore !!!
with open("token.txt", "r") as f:
    token = f.read().strip()

if not token:
    raise RuntimeError("Token nije definisan. Prekidamo.")

client.run(token)