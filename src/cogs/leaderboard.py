# Local
try:
    from .helpers import config
except ImportError:
    import helpers.config

import time
import discord

from discord.ext import commands

class Leaderboard(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='🔧Zeigt die aktivsten Nutzer im Server an!')
    async def leaderboard(self, ctx):
        users = {}

        for channel_id in config.load()['commands']['leaderboard']['chat_channel_ids']:
            if channel_id in [c.id for c in ctx.guild.channels]: # correct server
                async for message in self.client.get_channel(channel_id).history(limit=500):
                    if message.author.bot:
                        return
                    try:
                        users[message.author.mention] += 1
                    except KeyError:
                        users[message.author.mention] = 1
        
        users = sorted(users.items(), key=lambda x:x[1], reverse=True)
        users = dict(users[:10])

        emojis = [':first_place:', ':second_place:', ':third_place:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:']

        text = '**Die Nutzer mit den meisten Nachrichten*:\n**'
        place = 0   
        for user in list(users.keys()):
            text += f'{emojis[place]} {user} **{users[user]}** \n'
            place += 1

        await ctx.send(embed=discord.Embed(title='Rangliste', description=text, color=config.load()['design']['colors']['primary']).set_footer(text='*Zählt nur die letzten 500 Nachrichten in Chatkanälen.'))

def setup(client):
    client.add_cog(Leaderboard(client))