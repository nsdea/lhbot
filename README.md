![Cover](media/lh_cover.png)

# Community Bot
The following statistics are **fully automatic and 100% up to date!** 
### Repository
![Could not load repository](https://img.shields.io/github/contributors/nsde/lhbot)
![Could not load repository](https://img.shields.io/github/commit-activity/m/nsde/lhbot)
![Could not load repository](https://img.shields.io/github/last-commit/nsde/lhbot)

### Code
![Could not load repository](https://img.shields.io/github/languages/top/nsde/lhbot)
![Could not load repository](https://img.shields.io/github/license/nsde/lhbot)
![Could not load repository](https://img.shields.io/github/repo-size/nsde/lhbot)
### Security & Stability
![Could not load repository](https://img.shields.io/snyk/vulnerabilities/github/nsde/lhbot)
![Could not load repository](https://img.shields.io/github/issues-raw/nsde/lhbot)
![Could not load repository](https://img.shields.io/scrutinizer/quality/b/nsde/lhbot)

### Features
![Could not load repository](https://img.shields.io/github/search/nsde/lhbot/@commands.command?label=Commands)
![Could not load repository](https://img.shields.io/github/search/nsde/lhbot/@commands.Cog.listener?label=Event%20Listeners)
![Could not load repository](https://img.shields.io/github/search/nsde/lhbot/client.add_cog?label=Cogs%20%28Extensions%29)

### Join our Discord community!
![Loading...](https://img.shields.io/discord/623157804013715456?label=Discord)
# Contribute to support us!

## Requirements
- Some coding knowledge (*Python*, *Git(Hub)*, *IDEs*, *Discord*,...)
- If you're not familiar with most of the terms listed above, you may watch some tutorials or ask us first
  - German tutorials:
    - DiscordPy-Serie: https://www.youtube.com/playlist?list=PLNmsVeXQZj7rI3usLYlWhsjdFJ-MER_pU
    - DiscordPy-Einführung: https://youtu.be/GL57VWBV8g0
    - Git (langes Tutorial): https://youtu.be/uGLQF2kUwOA
    - Git (kurzes Tutorial); https://youtu.be/elh1y6laO8I

  - English tutorials:
    - Tutorial series: https://youtu.be/nW8c7vT6Hl4
    - Full one-hour course: https://youtu.be/SPTfmiYiuok
    - Git (short tutorial): https://youtu.be/USjZcfj8yxE
    - Git (long tutorial): https://youtu.be/RGOj5yH7evk
    - https://www.techwithtim.net/tutorials/discord-py/
    - https://realpython.com/how-to-make-a-discord-bot-python/

### Software
- An **IDE**, e.g. *Visual Studio Code*, *PyCharm* or *Sublime Text*
- ***Python*** installation
  - Should be `3.7`-`3.9`
  - `3.8.10` is recommended
- ***pip*** (the package manager for *Python*)
- ***git*** (you may also connect it with your IDE using an extension)
- Up-to-date **operating system** (OS)
  - *Ubuntu Linux* is recommended, *Windows* should also work (Windows 10 or above is recommended)

### Hardware
- Pretty much everything will work fine
## How to get started
- Download the source code & unzip it with whatever tool you want to (e.g. 7zip, WinRar)
- Get yourself a **bot token**, so you can access the bot
    - You can either ask us, or
    - create a testing bot (recommended option), here's how (this only needs to be done ONCE):
      - Go to the [Discord Developer Portal](https://discord.com/developers/applications) (you maybe need to sign in)
      - Create a **new application** by clicking the bottom on the top right
      - Give it a **name** & create it
      - Go to the *Bot* tab
      - **Add a bot** by clicking the blue button
      - Scroll down and activate the following:
        - *Presence Intent*
        - *Server Members Intent*
      - Make sure to **save changes** whenever asked to!
      - Scroll down to *OAuth2 URL Generator* and select *bot* (in the middle)
      - You can change the **bot permissions** at the bottom if you wish to
      - Copy the **bot invite URL** by clicking *Copy* under the *Scopes*-Section
      - **Invite the bot** to your testing-server by entering the URL and following the steps on screen
      - Finally, go to the *Bot*-Tab in the *Developer Portal* and **copy the client token** (blue button "Copy" at the top left)

- **Rename** the `dotenv_template.txt` to `.env` and change its values according to the template, keep in mind: 
   > The content of `.env` is **top secret!** Don't give anyone access to it.
- Install all needed packages using `pip install -r requirements.txt`
- To **start the bot**, run `src/bot.py` using the terminal.
- GLHF!
## Commands

| Commands | Example | Description | Authorization | Status |
| ------ | ------ |  ------ | ------ | ------ |
| !meme | !meme | Sends a meme | @everyone  | 🔴 |
| !game | !game | A little game | @everyone  | 🔴 |
| !ban | !ban "@USER" | Ban a user | @owner  | 🟢 |
| !unban | !unban "@USER" | Unban the user | @owner  | 🟢 |
| !mute | !mute "@USER" | Mute a user | @owner  | 🟠 |
| !unmute | !unmute "@USER" | Unmute a user | @owner  | 🟠 |
| !set | !set join "#channel", !set leave "#channel" | Sets the channel in which the (welcome / leave) messages are sent to. | @owner  | 🔴 |
| !del | !del join "#channel", !del leave "#channel" | Removes the channel in which the (welcome / leave) messages are sent to. | @owner  | 🔴 |
| !help | !help | Shows a help page | @everyone  | 🔵 |
| !prefix | !prefix "new prefix" | Changes the prefix to "prefix". | @owner | 🔴 |
| !info | !info "@USER", !serverinfo, !info server | Shows information about the server as well as about the user. | @everyone | 🟡 |
| !leaderboard | !leaderboard, !leaderboard invites, leaderboard activity | Shows a ranking of the most active users or with the most invites. | @everyone | 🟢 |
| !verify | !verify "#channel" | Sets the channel in which the verification query will be made | @owner | 🔴 |

### Legend

🔴 **Will be done later**
> **Note:** Some commands have this label, because the bot can be configured using the `config.yml`  

🟠 **To-do**

🟡 **Working on it**

🟢 **Ready for use**

🔵 **Fully functional**

******


## Troubleshooting
### No permissions
The bot might not have the correct permissions.
An exception should appear in the console saying:
```py
discord.errors.Forbidden: 403 Forbidden (error code: 50013): Missing Permissions
```
In this case, make sure the bot has **Administrator** permissions and has a very high role:
- Go to **Server Settings**
- Open the **Roles** Tab
- Add a role to the bot and move it all the way to the top
## JoinMessage Example

```python
@client.event
async def on_member_join(member):

    embed = discord.Embed(title=f"Willkommen {member.display_name}",
                          description=f"Im Kanal {client.get_channel(ytChannel).mention} wirst du immer die neusten Videos von LH Cyber Security finden. Um dir Self Roles zuzuweisen gehe in den Channel {client.get_channel(settingsChannel).mention} und wähle da deine Themen aus. Schau dich einfach mal um und bei Fragen stehen wir dir gerne zur Verfügung. Das LH Team wünscht dir {member.mention} einen angenehmen Aufenthalt.",
                          embed=discord.Embed(color=0xfefbfb),
                          timestamp=datetime.datetime.utcnow()
                          )

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/707638208124682260/764405331182485514/LH_Logo.png"
    )

    embed.set_footer(text='Community Bot', icon_url='https://media.discordapp.net/attachments/707638208124682260/764405331182485514/LH_Logo.png')

    await client.get_channel(joinChannel).send(embed=embed)

```

 ## Verify Command

```python
import discord
from discord.ext import commands

TOKEN = ""
owner_ids = [334567239342620675, 338711554683830292]
role = "Member" #Rolle nach verifikation
status = ['LH Bot', 'Protects the Discord', 'Verification Bot']
queue = []
welcome_channel_id = 707638208124682260
bot = commands.Bot(command_prefix='!', owner_id=owner_ids)
bot.remove_command('help')

#Wenn Bot gestartet
@bot.event
async def on_ready():
    welcome_channel = bot.get_channel(welcome_channel_id)
    print(f"Eingeloggt als: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n")
    await bot.change_presence(status=discord.Status.online)
    print('Erfolgreich gestartet...\n')
    print('Events:\n\n')

#Wenn Bot gestopt
@bot.command(name='stop', aliases=['shutdown'])
async def stop(ctx):
    if ctx.author.id in bot.owner_id:
        await ctx.send('Bot stoppt...')
        await bot.close()

#Wenn !verify
@bot.command(name='verify')
@commands.has_permissions(administrator=True)
async def verify(ctx):


    embed = discord.Embed(colour=discord.colour.Colour.blue(),
                          url="https://media.discordapp.net/attachments/707638208124682260/764118143429771314/LH_Logo.png")
    embed.set_author(name="Verification Bot",
                     url="https://www.youtube.com/channel/UCe4PsvZK8Tdn1R3M-j-bqOQ",
                     icon_url="https://media.discordapp.net/attachments/707638208124682260/764118143429771314/LH_Logo.png")
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/707638208124682260/764118143429771314/LH_Logo.png")
    embed.add_field(name="Bitte klicke auf :white_check_mark: um deinen Account zu verifizieren.",
                    value="Wenn du Problem hast mit der Verifikation kontaktiere einen Admin.", inline=True)

    await ctx.send(embed=embed)

#Rollen verteilung
@bot.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "✅": 
        Member = discord.utils.get(user.guild.roles, name=Member)
        await user.add_roles(Member)



#Bot Token
bot.run(TOKEN)
```

----------







## Links
[![N|Solid](Images/Discord.png)](https://discord.gg/aUP35py)
