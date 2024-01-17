import discord
from discord.ext import commands
import datetime

BOT_TOKEN = ""
BOT_NAME = "sebby-bot"

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print("bot is ready")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
@commands.has_role("ALL POWERFUL")
async def ban(ctx, member:discord.Member, *, reason):
    if reason == None:
        reason = "This user was banned by " + ctx.message.author.name
    await member.ban(reason+reason)
    embed=discord.Embed(title="Banned", description=f"Banned {member} for {reason}".format(ctx.message.author), color=0xff00f6)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role("Admin", "ALL POWERFUL")
async def kick(ctx, member:discord.Member, *, reason):
    if reason == None:
        reason = "This user was kicked by " + ctx.message.author.name
    await member.kick(reason+reason)
    embed=discord.Embed(title="Kicked", description=f"Kicked {member}".format(ctx.message.author), color=0xff00f6)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role("Admin", "ALL POWERFUL")
async def mute(ctx, member:discord.Member, timelimit):
    if "s" in timelimit:
        gettime = timelimit.strip("s")
        newtime = datetime.timedelta(seconds=int(gettime))
    await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
    

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description=f"""
    Commands:
    kick [USERNAME] [REASON] - kicks user
    ban [USERNAME] [REASON]  - bans user
    hello                    - says hello
    help                     - shows this
    """.format(ctx.message.author), color=0xff00f6)
    await ctx.send(embed=embed)

bot.run(BOT_TOKEN)
