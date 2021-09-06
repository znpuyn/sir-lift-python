import discord
from discord.utils import get
from discord.ext import commands
intents = discord.Intents.all()
intents.members = True

token = open("key.txt", "r")
bot = commands.Bot(command_prefix='$', intents=intents)

#Startup
@bot.event
async def on_ready():
    print("Fully initialized, logged on as {lift.user}".format(bot))

@bot.event 
async def on_disconnect():
    print ("I have lost connection, please troubleshoot")






#run code
bot.run(token.read())