from .helpers import config # saves time using a YAML function 
from .helpers import youtube
from .helpers import fancyfont

import discord
import asyncio

from discord.ext import commands

class YouTubeTools(commands.Cog):
    def __init__(self, client):
        self.client = client

        async def ten_minute_loop():
            await client.wait_until_ready()
            while not client.is_closed():
                data = youtube.channel_data()
                subs_text = f'🔥 {fancyfont.bold(data["subs"])} 𝐀𝐛𝐨𝐬'
                views_text = f'📺 {fancyfont.bold(data["views"])} 𝐀𝐮𝐟𝐫𝐮𝐟𝐞'
                videos_text = f'📽️ {fancyfont.bold(data["videos"])} 𝐕𝐢𝐝𝐞𝐨𝐬' 

                for guild in self.client.guilds:
                    for channel in guild.channels:
                        if channel.name.startswith('🔥') and channel.name.endswith('𝐀𝐛𝐨𝐬'):
                            await channel.edit(name=subs_text)
                        if channel.name.startswith('📺') and channel.name.endswith('𝐀𝐮𝐟𝐫𝐮𝐟𝐞'):
                            await channel.edit(name=views_text)
                        if channel.name.startswith('📽️') and channel.name.endswith('𝐕𝐢𝐝𝐞𝐨𝐬'):
                            await channel.edit(name=videos_text)

                await asyncio.sleep(60*10)

        self.client.loop.create_task(ten_minute_loop())

def setup(client):
    client.add_cog(YouTubeTools(client))