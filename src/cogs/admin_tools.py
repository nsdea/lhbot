# Local
from .helpers import config

import discord

from discord.ext import commands

class AdminTools(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.prefix = config.load()['bot']['prefix']

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['config', 'settings'], help='🔒Ändere die Bot-Einstellungen. [Benötigt die Berechtigung "administrator"]', usage='Kein Argument für Infos und Hilfe angeben.')
    async def configure(self, ctx, *args):
        args = ' '.join(args)

        if args.strip(' '):
            path = args.split(' = ')[0].split()
            to = args.split(' = ')[1]

            config.edit(path=path, to=to)
            await ctx.send(embed=discord.Embed(title='Einstellung vorgenommen!', description=f'> `{" ".join(path)}` wurde auf **`{to}`** gesetzt!', color=config.load()['design']['colors']['primary']))

        else:
            await ctx.send(embed=discord.Embed(title='Wie die Einstellungen funktionieren', description=f'> **Argumente:** `{self.prefix}config <Pfad, mit Leerzeichen getrennt> <Wert>`,\n> **Beispiel:** `{self.prefix}config bot prefix $`\n(Manche Einstellungen benötigen einen Neustart!)\n**__Aktuelle Einstellungen__**\n\n```yml\n{open("src/config.yml").read()}```'))

def setup(client):
    client.add_cog(AdminTools(client))