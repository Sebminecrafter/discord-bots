from discord.ext import commands
import discord

BOT_TOKEN = ""
BOT_NAME = "sebby-bot"

client = discord.Client()
bot = commands.Bot(command_prefix="?", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print("bot is ready")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def ban(ctx, user, reason):
    await ctx.send(f"/ban {user} {reason}")
    embed=discord.Embed(title="Banned", description=f"Banned {user} for {reason}".format(ctx.message.author), color=0xff00f6)
    await ctx.send(embed=embed)

@bot.command()
async def kick(ctx, user):
    await ctx.send(f"/kick {user}")
    embed=discord.Embed(title="Kicked", description=f"Kicked {user}".format(ctx.message.author), color=0xff00f6)
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description=f"""
    Commands:
    kick [USERNAME]          - kicks user
    ban [USERNAME] [REASON]  - bans user
    hello                    - says hello
    help                     - shows this
    """.format(ctx.message.author), color=0xff00f6)
    await ctx.send(embed=embed)

@client.event
async def on_message(msg):

client.run(BOT_TOKEN)
bot.run(BOT_TOKEN)
