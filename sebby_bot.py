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
        if int(gettime) > 2419000:
            await ctx.send("Mute cannot last longer than 28 days.")
        else:
            newtime = datetime.timedelta(seconds=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
    elif "m" in timelimit:
        gettime = timelimit.strip("m")
        if int(gettime) > 40320:
            await ctx.send("Mute cannot last longer than 28 days.")
        else:
            newtime = datetime.timedelta(seconds=int(gettime*60))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
    elif "h" in timelimit:
        gettime = timelimit.strip("h")
        if int(gettime) > 672:
            await ctx.send("Mute cannot last longer than 28 days.")
        else:
            newtime = datetime.timedelta(seconds=int(gettime*60*60))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
    elif "d" in timelimit:
        gettime = timelimit.strip("d")
        if int(gettime) > 28:
            await ctx.send("Mute cannot last longer than 28 days.")
        else:
            newtime = datetime.timedelta(seconds=int(gettime*60*60*24))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)

@bot.command()
@commands.has_any_role("Admin", "ALL POWERFUL")
async def unmute(ctx, member:discord.Member):
    await member.edit(timed_out_until=None)

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
