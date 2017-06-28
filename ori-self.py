#!/usr/bin/env python3
import discord, json
from discord.ext import commands
from platform import python_version
from printoverride import print

jsonfile = "selfbot"

try:
    with open('./{}.json'.format(jsonfile), 'r+') as secretfile:
        sec = json.load(secretfile)
        token = sec['bot']['token']
except FileNotFoundError:
    exit("{}.json is not in the current bot directory.".format(jsonfile))

startup_extensions = ['ADMIN','General']
description = "Ori's self-bot for Discord (API v{0}) written in Python3 (v{1}).".format(discord.__version__,python_version())

bot = commands.Bot(command_prefix='~', description=description, self_bot=True)

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.NoPrivateMessage):
        await bot.send_message(discord.Object(id="{0}".format(ctx.message.channel.id)), 'This command cannot be used in private messages.')
    elif isinstance(error, commands.DisabledCommand):
        await bot.send_message(discord.Object(id="{0}".format(ctx.message.channel.id)), 'Sorry. This command is disabled and cannot be used.')
    elif isinstance(error, commands.CommandInvokeError):
        print('In {0.command.qualified_name}:'.format(ctx), file=sys.stderr)
        traceback.print_tb(error.original.__traceback__)
        print('{0.__class__.__name__}: {0}'.format(error.original), file=sys.stderr)


@bot.event
async def on_ready():
    onlineMSG = "* Logged in as '{0}' ({1}). *".format(bot.user.name,bot.user.id)
    dversionMSG = "Discord API v{0}".format(discord.__version__)
    pversionMSG = "Python3 v{0}".format(python_version())
    onDIV = '*'
    while len(onDIV) < len(onlineMSG):
        onDIV = onDIV + '*'
    onLEN = len(onlineMSG) - 2
    while len(dversionMSG) < onLEN:
        dversionMSG = ' ' + dversionMSG
        if len(dversionMSG) < onLEN:
            dversionMSG = dversionMSG + ' '
    dversionMSG = '*' + dversionMSG + '*'
    while len (pversionMSG) < onLEN:
        pversionMSG = ' ' + pversionMSG
        if len(pversionMSG) < onLEN:
            pversionMSG = pversionMSG + ' '
    pversionMSG = '*' + pversionMSG + '*'
    print("{0}\n{1}\n{2}\n{3}\n{0}".format(onDIV,onlineMSG,dversionMSG,pversionMSG))
    if __name__ == '__main__':
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
                print('Loaded extension: {}'.format(extension))
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__,e)
                print('Failed to load extension: {}\n{}'.format(extension,exc))

@bot.event
async def on_message(message):
    await bot.process_commands(message)

bot.run(token,bot=False)