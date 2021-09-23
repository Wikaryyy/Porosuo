import discord
import random
import time
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
    curMembers = []
    memberNames = []
    teams = [fTeam, sTeam]
    channel = client.get_channel(channelsID)
    for member in channel.members:
      memberNames.append(member.name)
    pass
    embed = discord.Embed(title="Customs", color=0x91b9ee)
    embed.set_author(
        name="Porosuo", icon_url="https://cdn.discordapp.com/attachments/889986914885726229/890240446675177492/poro_harnold.jpg")
    print("Czas wykonania Komendy Customki[ "+str(time.ctime(time.time()))+"]")
    print("Kanał na którym znajdują się gracze:" +
          (ctx.message.author.voice.channel.name))
    print("Lista osób na kanale: " + "[ " +', '.join(memberNames)+ " ]")
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
        embed.add_field(name="Za mało graczy", value="1", inline=False)
    await ctx.send(embed=embed)

keep_alive()
client.run(os.environ['TOKEN'])
