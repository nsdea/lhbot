from cogs.helpers import config

import os
import dotenv
import socket
import discord

from discord.ext import commands

dotenv.load_dotenv()  # initialize virtual environment

COLOR = config.load()['design']['colors']['primary']  # primary color for embeds
TESTING_MODE = socket.gethostname() in config.load()['bot']['testing_device_names']  # testing systems
PREFIX = config.load()['bot']['prefix']  # command prefix

# create bot, help_command is none because it's a custom one
client = commands.Bot(
    command_prefix=commands.when_mentioned_or(PREFIX), help_command=None, intents=discord.Intents.all())

@client.event
async def on_ready():
    print('ONLINE as', client.user)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='LH\'s videos!'))

@client.event
async def on_command_error(ctx, error):
    # error: 'error message'
    error_messages = {
        commands.CheckFailure: 'There was a problem with a check.',
        commands.UserInputError: 'There was a problem with your input.',
        commands.CommandNotFound: f'Command not found. Use **`{PREFIX}help`** for a list of commands.',
        # the f-string generates the help-command for the command
        commands.MissingRequiredArgument: f'Oops, I think you [*forgo**r*** 💀](https://i.redd.it/mc9ut2313b571.jpg) an argument, go check it using **`{PREFIX}help {ctx.message.content.replace(PREFIX, "").split()[0]}`**',
        # the f-string generates the help-command for the command
        commands.TooManyArguments: f'You gave too many arguments, use this command for help: **`{PREFIX}help {ctx.message.content.replace(PREFIX, "").split()[0]}`**',
        commands.Cooldown: 'Please be patient :)',
        # commands.MessageNotFound: 'This message could not be found.',
        # commands.ChannelNotFound: 'This channel could not be found.',
        commands.NoPrivateMessage: 'This does not work in DM channels.',
        commands.MissingPermissions: 'Sorry, you don\'t have the following permission(s) to do this:',
        commands.BotMissingPermissions: 'Sorry, I don\'t have the following permission(s) to do this:',
        commands.ExtensionError: 'This is probably a bug you can\'t do anything about, but there was a problem with an extension.',
        # the f-string generates the help-command for the command
        commands.BadArgument: f'There was a problem converting one of the argument\'s type, use this command for help: **`{PREFIX}help {ctx.message.content.replace(PREFIX, "").split()[0]}`**',
    }

    error_msg = 'Unknown error.'

    # create the error message using the dict above
    for e in error_messages.keys():
        if isinstance(error, e):
            error_msg = error_messages[e]

    # other errors:
    # - too long
    if 'Invalid Form Body' in str(error):
        error_msg = 'Sorry, I can\'t send messages that long due to Discord limitations.'

    # - bug
    if 'Command raised an exception' in str(error):
        error_msg = 'Oops, our developers maybe messed up here. This is probably a bug.'

    # add detailed info
    if isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions):
        error_msg += f'\n**`{", ".join(error.missing_perms)}`**\n'

    # add full error description formatted as a code text
    error_msg += '\n\n__Error message:__\n```\n' + str(error) + '\n```'

    # create a cool embed
    embed = discord.Embed(
        title='Command Error',
        description=error_msg,
        color=0xFF0000
    )

    # send it
    await ctx.send(embed=embed)
    if TESTING_MODE or error_msg == 'Unknown error.':
        raise error  # if this is a testing system, show the full error in the console

# help command
# pretty much copy and pasted from *my* bot "NeoVision"
# but nobody cares, I mean, it's cool and useful
# so... I guess everything is fine


@client.command(aliases=['command', 'commands', 'help'], help='📃Display info about commands.', usage='(<command name>)')
async def commandinfo(ctx, name=None):
    if name:
        for c in client.commands:
            if name.lower() == c.name or name.lower() in list(c.aliases):
                text = f'''
        **Help:** {c.help if c.help else ' - '}
        **Usage:** {c.usage if c.usage else ' - '}
        **Aliases:** {', '.join(c.aliases) if c.aliases else ' - '}
        '''
                embed = discord.Embed(
                    title='Command ' + c.name, color=COLOR, description=text)
                await ctx.send(embed=embed)

                return

        embed = discord.Embed(title='Command not found', color=COLOR,
                              description='This command does not exist...')
        await ctx.send(embed=embed)

    else:
        def sortkey(x):
            return x.name

        categories = {'🚨': 'Main commands', '📃': 'Information and help',
                      '🔧': 'Tools and utilities', '🔒': 'Special', '🔩': 'Other'}

        # ok, somehow I managed to get this to work, don't ask me how, but it WORKS
        text = ''
        for category in categories.keys():
            text += f'\n{category} **{categories[category]}**\n'
            for command in sorted(client.commands, key=sortkey):
                if command.help.startswith(category):
                    if command.aliases:
                        text += f'{command.name} *({"/".join(command.aliases)})*\n'
                    else:
                        text += f'{command.name}\n'
                    continue
                # if category == '✨' and command.help[0] not in categories.keys():
                #   if command.aliases:
                #     text += f'{command.name} *({"/".join(command.aliases)})*\n'
                #   else:
                #     text += f'{command.name}\n'

        embed = discord.Embed(title='Commands', color=COLOR, description=text)
        embed.set_footer(
            text=f'Run {PREFIX}help <command> for detailed info on a command')
        await ctx.send(embed=embed)

# load cogs
# credit: https://youtu.be/vQw8cFfZPx0
for filename in os.listdir(os.getcwd() + '/src/cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('DISCORD'))  # run bot with the token set in the .env file
