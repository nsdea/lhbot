# Local
try:
    from .helpers import config
except ImportError:
    import helpers.config

import time
import discord

from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='🔧Die beliebtesten r/memes Posts!')
    async def meme(self, ctx):
        pass
    
def setup(client):
    client.add_cog(Fun(client))