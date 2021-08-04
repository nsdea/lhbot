# local
from .helpers import challenges

import discord
import asyncio

from discord.ext import commands

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(help='🔧Zeige eine Demo für die Verifizierung an.')
    async def verifydemo(self, ctx):
        challenge = challenges.get_challenge()
        await ctx.send(embed=discord.Embed(title='Verification Challenge Demo', description=challenge[0], color=discord.Color(0x00FFFF)).set_footer(text=f'Richtig wäre: {challenge[1]}'))

    @commands.has_permissions(manage_messages=True)
    @commands.command(help='🔧Löscht eine bestimme Anzahl von Nachrichten im aktuellen Kanal, kein Argument angeben, um alle Nachrichten in dem aktuellen zu löschen. Benötigt die "manage_messages" Berechtigung für sowohl den Bot, als auch für den Nutzer.', aliases=['purge'])
    async def clear(self, ctx, count=999999):
        are_you_sure_message = await ctx.send(delete_after=60, embed=discord.Embed(title='Bist du dir sicher?', description=f'Reagiere, um **{count if count != 999999 else "alle"}** Nachrichten in diesem Kanal zu löschen.\nDieser Vorgang kann nicht rückgängig gemacht werden.', color=discord.Color(0xFFFF00)).set_footer(text=f'Diese Nachricht wird nach 60 Sekunden gelöscht.'))
        
        await are_you_sure_message.add_reaction('☑️')

        def check(reaction, user):
            return reaction.message == are_you_sure_message and user == ctx.author

        try:
            await self.client.wait_for('reaction_add', check=check, timeout=60)
        except asyncio.TimeoutError: # Zeit abgelaufen?
            return
        else:
            await ctx.channel.purge(limit=count)
            await ctx.send(delete_after=5, embed=discord.Embed(title=':wastebasket: Chat gepurged!', description=f'**{count if count != 999999 else "Alle"}** Nachrichten im Kanal sollten jetzt weg sein! :)', color=discord.Color(0x00FF00)).set_footer(text=f'Diese Nachricht wird nach 5 Sekunden gelöscht.'))

def setup(client):
    client.add_cog(Tools(client))