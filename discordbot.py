from discord.ext import commands
import os
import traceback
import json
import requests

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

base_url = 'https://public-api.tracker.gg/v2/apex/standard/'
endpoint = base_url + 'profile/' + 'origin/mojyapizza'

params = {
        'TRN-Api-Key': '55abf24b-1a28-4165-8e67-3747c0d9deb8'
        }
    
def countKills():
    session = requests.Session()
    req = session.get(endpoint, params=params)
    req.close()
    profile = json.loads(req.text)

    for i in range(len(profile['data']['segments'])):
        if profile['data']['segments'][i]['metadata']['name'] == 'Wattson':
            kills = profile['data']['segments'][i]['stats']['season7Kills']
    return kills


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    # await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def andyu(ctx):
    await ctx.send(countKills())


bot.run(token)
