import json
import time
import discord

from discord.ext import commands

class AntiRaid(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='')
    async def on_member_join(self, member):
        open(f'temp/joins/{member.guild.id}.log', 'a').write(f'\n{time.time()}')

def setup(client):
    client.add_cog(AntiRaid(client))