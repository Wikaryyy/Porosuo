import discord
import random
import numpy
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents().all()

# 889969405776261154
client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


async def on_message(message):
    if message.author == client.user:
        return


@client.command()
async def customki(ctx):
    channelsID = ctx.message.author.voice.channel.id
    fTeam = []
    sTeam = []
    teams = [fTeam, sTeam]
    embed = discord.Embed(title="Customs", color=0x0c8336)
    embed.set_author(
        name="Porosuo", icon_url="https://cdn.discordapp.com/attachments/889986914885726229/890240446675177492/poro_harnold.jpg")
    channel = client.get_channel(channelsID)
    curMembers = []
    if(len(channel.members) > 1):
        for member in channel.members:
            curMembers.append(member)
        for member in curMembers:
            if len(sTeam) == len(fTeam):
                random.choice(teams).append(member.mention)
            elif len(sTeam) > len(fTeam):
                fTeam.append(member.mention)
            else:
                sTeam.append(member.mention)
        pass
        print(str(curMembers))

        print("Pierwszy T: " + str(fTeam))
        print("Drugi T: " + str(sTeam))
        embed.add_field(name="Pierwszy Team",
                        value=', '.join(fTeam), inline=False)
        embed.add_field(name="Drugi Team",
                        value=', '.join(sTeam), inline=False)
    else:
        embed.add_field(name="Za mało graczy", value="0", inline=False)
    await ctx.send(embed=embed)

keep_alive()
os.getEnv()
client.run(os.environ['TOKEN'])
