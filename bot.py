import requests
from discord.ext import commands

bot = commands.Bot(command_prefix="/")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)


@bot.command()
async def ping(ctx, ip):
    text = requests.get('https://api.mcsrvstat.us/2/{}'.format(ip))
    data = text.json()
    motd = '\n'.join(data["motd"]["clean"])
    port = data["port"]
    players_online = data["players"]["online"]
    players_max = data["players"]["max"]
    version = data["version"]
    await ctx.channel.send('ip: {} \nport: {} \nmotd: \n{} \n \nplayers online: {} \nmax players: {} \nversion: {}'.format(ip, port, motd, players_online, players_max, version))


bot.run('key')
