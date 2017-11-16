#Peter Bot
#add the bot: discordapp.com/oauth2/authorize?client_id=380055447240966144&scope=bot&permissions=0


import discord
import time
from discord.ext import commands
import random



description = "The one and only Peter Bot.."
bot_prefix = "Peter."
client = commands.Bot(description=description, command_prefix=bot_prefix)
commands = "Prefix = Peter.\n(Prefix)Pontus\n(prefix)Hello"


@client.event
async def on_ready():
    print("Executing order 66...")
    time.sleep(1.5)
    print("The bot is logged in")
    print("Bot name: {}".format(client.user.name))
    print("Bot ID: {}".format(client.user.id))
    print("Discord version: {}".format(discord.__version__))
    print("Executed order 66")
    await client.change_presence(game=discord.Game(name="Peter.Help"))


# Random shit
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Not Pont")


# Commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith(bot_prefix + "Pontus") or message.content.startswith("Pontus"):
        await client.send_message(message.channel, "Pentus*")
    elif message.content.startswith(bot_prefix + "Hello"):
        await client.send_message(message.channel, "Fuck you")
    elif message.content.startswith(bot_prefix + "Help"):
        await client.send_message(message.channel, commands)
    elif message.content.startswith(bot_prefix + "Die") or message.content.startswith(bot_prefix + "die"):
        await client.send_message(message.channel, "*Killing myself*")
        time.sleep(5)
        await client.send_message(message.channel, "Killed myself")
    elif message.content.startswith(bot_prefix + "Random Peter"):
        random_peter = random.randint(1,3)
        if random_peter == 1:
            await client.send_message(message.channel, "https://image.prntscr.com/image/Y1xii7BJQ-CFXyH7Z52aag.png")
        elif random_peter == 2:
            await client.send_message(message.channel, "https://image.prntscr.com/image/6hlVuMlSSP_TyWSGP-4ohg.png")
        elif random_peter == 3:
            await client.send_message(message.channel, "https://i.ytimg.com/vi/TZBlgOYQa5I/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLAVrR59JYvwLXZw3HXUVgLysMXdjg")
    elif message.content.startswith(bot_prefix + "Random Pontus") or message.content.startswith(bot_prefix + "Random Pentus"):
        random_pontus = random.randint(1,3)
        if random_pontus == 1:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/352750821894651906/380341430972973057/Pontus.jpg")
        elif random_pontus == 2:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/352750821894651906/380341995735875584/Pontus_2.jpg")
        elif random_pontus == 3:
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/352750821894651906/380343781742084097/12208683_1642080936043352_4707010062800228967_n.jpg")


        


# 8 ball:
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith(bot_prefix + "8Ball"):
        if len(message.content) - 11 >= 1:
            random_ball = random.choice(["Signs point to yes", "Without a doubt.",   "My sources say no.", "As I see it, yes.", "You may rely on it.", "Concentrate and ask again.", "Outlook not so good.", "It is decidedly so.", "Better not tell you now.", "Very doubtful.",  "Yes - definitely.",  "It is certain. ", "Cannot predict now.",  "Most likely.", "Ask again later.", "My reply is no.", "Outlook good.", "Don't count on it."])
            await client.send_message(message.channel, ":crystal_ball: " + (random_ball) )
        else:
            await client.send_message(message.channel, "Please ask a question")








client.run("Token Here")

