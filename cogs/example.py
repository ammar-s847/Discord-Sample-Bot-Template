import discord
from discord.ext import commands

class Example(commands.Cog) :
    def __init__(self, client) :
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self) :
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Hello There!')) # Use this to change the 'game' status of the bot
        print("Example Cog is working") # prints to the console.
    
    @commands.command(aliases = ['showPing']) # Aliases are alternative ways of calling a command.
    async def ping(self, ctx) :
        await ctx.send(f"Ping: {round(1000 * self.client.latency)}ms") # responds to the user when ping command is mentioned. ex: ".ping"
        print(f"{str(ctx.message.author)} asked for the Ping")
        print(str(ctx.message.author)) # prints name of the user who mentioned the bot to the console.
        print(str(ctx.message.channel)) # prints the channel of the server in which the bot was mentioned on to the console.
        print(str(ctx.message.content)) # prints the content of the mention to the console.

def setup(client) :
    client.add_cog(Example(client))