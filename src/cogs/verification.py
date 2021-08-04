# local imports
from .helpers import config # saves time using a YAML function 
from .helpers import challenges # generates random verification challenges for the user to solve

import discord
import asyncio

from discord.ext import commands

class Verification(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member): # someone joins the server        
        for channel_id in config.load()['system']['verification']['channel_ids']: # for every single verification channel
            verification_channel = await self.client.fetch_channel(channel_id) # create object to work with
            if verification_channel in member.guild.channels: # if the Discord server has this channel 
                challenge = challenges.get_challenge_with_embed() # generate verification challenge
                verification_messages = []
                
                verification_messages.append(await verification_channel.send(delete_after=config.load()['system']['verification']['timeout_seconds'], content=member.mention, embed=challenge[0])) # send embed message

                def message_check(message):
                    return message.author == member

                try:
                    await self.client.wait_for('message', check=message_check, timeout=config.load()['system']['verification']['timeout_seconds'])
                except asyncio.TimeoutError: # time's up
                    await verification_messages.append(verification_channel.send(delete_after=10, content=member.mention, embed=discord.Embed(title='Zeit abgelaufen!', color=config.load()['design']['colors']['primary'], description=f'Die Zeit für die Verifizierungsaufgabe ist leider abgelaufen.')))
                    return
                else: # user sent something:
                    
                    async for message in verification_channel.history():
                        if message.author == member:
                            sent = message
                            break

                    correct = challenge[1]
                    verification_messages.append(sent)

                    if sent.content == correct:
                        color = config.load()['design']['colors']['primary']
                        verification_messages.append(await verification_channel.send(content=member.mention, embed=discord.Embed(color=color, title=':white_check_mark: Erfolgreich verifiziert!', description=':tada: Herzlichen Glückwunsch, du wurdest soeben erfolgrech verifiziert.\nViel Spaß!')))

                        for role_id in config.load()['system']['verification']['role_id_on_success']: # for every single verification role
                            verification_role =  member.guild.get_role(role_id) # create object to work with
                            if verification_role in member.guild.roles: # if the Discord server has this role 
                                await member.add_roles(verification_role)
                    else:
                        color = 0xFF0000
                        verification_messages.append(await verification_channel.send(content=member.mention, embed=discord.Embed(color=color, title=':x: Das ist leider falsch!', description='Du hast die Verifizierungsaufgabe leider nicht bestanden. Sorry ¯\_(ツ)_/¯')))

                    await asyncio.sleep(10)

                    for msg in verification_messages:
                        await msg.delete()
def setup(client):
    client.add_cog(Verification(client))