# Local
try:
    from .helpers import config
except ImportError:
    import helpers.config

from .helpers import quiz

import os
import random
import discord
import asyncio
import asyncpraw

from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.reddit_client = asyncpraw.Reddit(
            client_id=os.getenv('REDDIT_ID'),
            client_secret=os.getenv('REDDIT_SECRET'),
            password=os.getenv('REDDIT_PASSWORD'),
            user_agent='Discord',
            username=os.getenv('REDDIT_USERNAME'),
        )

    @commands.command(aliases=['memes', 'meme'], help='🎮Die beliebtesten Posts von einem Subreddit (standardmäßig r/memes)!', usage='(<subreddit (ohne r/)>) (<randomizer>)')
    async def reddit(self, ctx, sub='memes|dankmemes|ich_iel|wholesomememes|okbuddyretard|comedyheaven|meme', randomizer=60):
        async def send(ctx=ctx, sub=sub, randomizer=randomizer):
            msg = await ctx.send(embed=discord.Embed(title='Einen Augenblick...').set_footer(text='Tipp: Falls es zu lange lädt, stelle das Argument "randomizer" niedriger (30), falls die Bilder oft die gleichen sind, stelle "randomizer" höher.'))

            BASE_URL = 'https://reddit.com'
            
            sub_name = sub
            if '|' in sub:
                sub_name = random.choice(sub.split('|'))
            subreddit = await self.reddit_client.subreddit(sub_name)

            posts = []

            async for p in subreddit.top(random.choice(['day', 'week', 'month']), limit=randomizer):
                if random.randint(0, len(posts)) > randomizer: # to speed up
                    break

                if p.url.endswith('.jpg') and len(p.title) < 256:
                    posts.append(p)
            
            try:
                post = random.choice(posts)
            except:
                await ctx.send(embed=discord.Embed(title='Kein Reddit-Post gefunden', description='Versuche einen anderen Subreddit.', color=0xFF0000))
                return

            embed = discord.Embed(
                color=config.load()['design']['colors']['primary'],
                url=BASE_URL + post.permalink,
                title=post.title,
                description=f'**Upvotes:** {round(post.score/1000, 1)}K ({post.upvote_ratio*100}%)',
                timestamp=datetime.fromtimestamp(post.created_utc)
            ).set_image(url=post.url).set_author(name=post.author).set_footer(text=f'r/{sub_name}')

            await msg.edit(embed=embed)

            return msg

        msg = await send()

        while True:
            await msg.add_reaction('▶️')
            
            def check(reaction, user): return reaction.message == msg and (not user.bot) and str(reaction) == '▶️'
            try:
                await self.client.wait_for('reaction_add', check=check, timeout=180)
            except asyncio.TimeoutError:
                return
            msg = await send()

    @commands.command(help='🎮Quiz spielen.')
    async def quiz(self, ctx):
        msg = await ctx.send(embed=discord.Embed(title='Quiz-Info', description='Willkommen bei dem **LH-Quiz**! Hier geht es um alles mögliche, was Software, Sicherheit & das Internet betrifft. Du hast für **jede Frage 10 Sekunden**. Außerdem gibt\'s **5 Fragen pro Quiz**.\nDu kannst das Quiz jederzeit mit :no_entry_sign: abbrechen und das Ergebnis anzeigen lassen.\n> Reagiere, um loszulegen!', color=config.load()['design']['colors']['primary']))

        await msg.add_reaction('☑️')

        def check(reaction, user): return reaction.message == msg and user == ctx.author

        try:
            await self.client.wait_for('reaction_add', check=check, timeout=60)
        except asyncio.TimeoutError:
            return

        already_asked = []
        quiz_dict = quiz.quiz_base()

        correct = 0
        count = 0
        while count < 5:
            for item in quiz_dict.keys():
                if item in already_asked:
                    quiz_dict.pop(item)

            question = random.choice(list(quiz_dict.keys()))
            already_asked.append(question)

            answer = quiz_dict[question][0]
            answers = random.shuffle(quiz_dict[question])
            
            msg = await ctx.send(embed=discord.Embed(title=question, description=f'1️⃣ {answers[0]}\n2️⃣ {answers[1]}\n3️⃣ {answers[2]}\n4️⃣ {answers[3]}', color=config.load()['design']['colors']['primary_dark']).set_footer(text='Du hast 10 Sekunden, viel Glück!'))

            for emoji in '1️⃣2️⃣3️⃣4️⃣🚫':
                await msg.add_reaction(emoji)
            
            def check(reaction, user):
                globals()['reacted'] = str(reaction.emoji)
                return reaction.message == msg and (not user.bot) and str(reaction) in '1️⃣2️⃣3️⃣4️⃣🚫'

            try:
                await self.client.wait_for('reaction_add', check=check, timeout=10)
            except asyncio.TimeoutError:
                await ctx.send(embed=discord.Embed(title='Zeit ist um!', description=f'Du hast leider nur 10 Sekunden für jede Frage.', color=0xFF0000))       
                continue

            if globals()['reacted']:
                correct += 1
            
            count += 1
        
        msg = await ctx.send(embed=discord.Embed(title='Quiz-Auswertung', description=f'Vielen Dank für deine Teilnahme!\n> **Ergebnis:** {correct}/5 richtig.', color=config.load()['design']['colors']['primary']))       

def setup(client):
    client.add_cog(Fun(client))