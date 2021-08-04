# Local
from .helpers import config
from .helpers import authorize

import time
import discord

from discord.ext import commands

class Authorization(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['connect'], help='⚙️LH Connect ist ein sicheres Verifizierungsverfahren, in dem eine Discord-Verbindung zum Nutzer hergestellt und überprüft wird.')
    async def auth(self, ctx, url=None):
        if url: # URL argument exists
            if isinstance(ctx.channel, discord.DMChannel): # command is being ran in a DM channel
                await ctx.reply(embed=discord.Embed(title='LH Connect - Wichtiger Hinweis!', description=f':warning: **Ganz wichtig! Lösche bitte deine Nachricht!**\nDies dient deiner eigenen Sicherheit.', color=0xFFFF00))

                auth_id = authorize.auth(url)
                if auth_id == ctx.author.id: # connected
                    await ctx.author.send(embed=discord.Embed(title='LH Connect - Erfolg', description=f':white_check_mark: Super! Dein Konto wurde **erfolgreich** mit *LH Connect* verbunden!', color=config.load()['design']['colors']['primary']))

                    for role_id in config.load()['system']['verification']['role_id_on_success']: # for every single verification role
                        verification_role =  ctx.author.guild.get_role(role_id) # create object to work with
                        if verification_role in ctx.author.guild.roles: # if the Discord server has this role 
                            await ctx.author.add_roles(verification_role)

                else: # error
                    await ctx.author.send(embed=discord.Embed(title='LH Connect - Fehler', description=':x: Leider konnte dein Konto **nicht verbunden** werden.\nVersuche es erneut (von Anfang an!), möglichweise musst du etwas warten.', color=0xFF0000))
            else:
                await ctx.message.delete()
                await ctx.send(content=ctx.author.mention, embed=discord.Embed(title='LH Connect - Sicherheit', description=':x: Aus Sicherheitsgründen kannst du die *connect*-URL nur per Privatnachricht senden.\nDeswegen wurde deine Nachricht gelöscht.', color=0xFF0000))

        else: # send setup URL
            auth_url = f'https://discord.com/api/oauth2/authorize?client_id={self.client.user.id}&redirect_uri=https%3A%2F%2Fgithub.com%2Fnsde%2Flhbot%2Fblob%2Fmain%2Fmarkdown%2Fconnect.md&response_type=code&scope=identify'
            await ctx.send(embed=discord.Embed(title='LH Connect - Setup', description=f':white_check_mark: Klicke auf den blauen Knopf "Autorisieren" und folge den Schritten.\n\n**{auth_url}**\n\nFalls nach dem Klicken auf den blauen Button "Autorisieren" die geöffnete Webseite leer ist, versuche, sie neu zu laden.', color=config.load()['design']['colors']['primary']))

def setup(client):
    client.add_cog(Authorization(client))