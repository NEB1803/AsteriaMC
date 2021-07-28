import discord
from mcstatus import MinecraftServer
from discord.ext import tasks
client = discord.Client ( intents = discord.Intents.all () )
server = MinecraftServer.lookup ( "139.99.125.7:25610" )

@client.event
async def on_ready():
    print ( 'We have logged in as {0.user}'.format ( client ) )

    await client.change_presence (
        activity = discord.Activity ( type = discord.ActivityType.playing, name = "AsteriaMC" ) )


@client.event
async def on_message(message):
    if ".modpack" in message.content:
        print ( ".modpack command was used by {0}".format( message.author.name ) )
        await message.add_reaction ( "✅" )
        modpack = discord.Embed (
            title = '**LEGENDSUNITED MODPACK**',
            description = '**MADE BY <@463831827128516608> \n https://www.mediafire.com/file/9dgkuazee1sou3p/LegendsUnited.zip/file3:',
            colour = discord.Colour.from_rgb ( 0, 255, 255 )
        )
        modpack.set_thumbnail ( url = "https://i.imgur.com/ZpjBCjM.png" )
        await message.channel.send ( embed = modpack )


    if "!ip" in message.content:
        print ( "!ip command was used by {0}".format ( message.author.name ) )
        await message.add_reaction ( "✅" )
        ip = discord.Embed (
            title = '**IP**',
            description = '**AsteriaMC**\nasteriamc.skynode.gg',
            colour = discord.Colour.from_rgb ( 0, 255, 255 )
        )
        ip.set_thumbnail ( url = "https://i.imgur.com/ZpjBCjM.png" )
        await message.channel.send ( embed = ip )

    if "!players" in message.content:

        try:
            temp1 = 1
            status = server.status ()
        except:
            await message.channel.send ( ":octagonal_sign: **AsteriaMC Server Is Offline**" )
            print ( ".players command was used by {0} (Server was offline)".format ( message.author.name ) )
            temp1 = 0
        if temp1 == 1:
            await message.channel.send ("**There are {0} Players currently playing on AsteriaMC SERVER**".format ( status.players.online ) )
            print ( "!players command was used by {0} ({1} Players were online)".format ( message.author.name,status.players.online ) )

    if ".status" in message.content:

        try:
            temp2 = 1
            status = server.status ()
        except:
            await message.channel.send ( ":octagonal_sign: **AsteriaMC Server Is Offline**" )
            print ( ".status was used by {0} (Server was offline)".format ( message.author.name ) )
            temp2 = 0
        if temp2 == 1:
            await message.channel.send ( ":white_check_mark: **AsteriaMC Server Is Online**" )
            print ( ".status command was used by {0} (Server was online)".format ( message.author.name ) )


@tasks.loop ( minutes = 5 )
async def send():
    stagechannel = client.get_channel ( 852475276701204500 )
    try:
        temp3 = 1
        status = server.status ()
    except:
        print ( "Server is offline postponed channel update" )
        await stagechannel.edit ( name = "Server Status: Offline" )
        temp3 = 0
    if temp3 == 1:
        print ( "Updated Server Players: {0}".format ( status.players.online ) )
        await stagechannel.edit ( name = "Server Players: {0}".format ( status.players.online ) )


@send.before_loop
async def before():
    await client.wait_until_ready ()


send.start ()

client.run ( "Nzc0MjUzNzY1OTU1NTUxMjMz.X6VGAg.xdiq6AfrjyEnoGqL9HGoUZVFo-o" )
