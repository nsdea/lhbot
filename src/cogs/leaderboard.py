import yaml
import time
import discord

from discord.ext import commands

class Leaderboard(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Leaderboard(client))