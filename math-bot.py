from discord.ext import commands
import discord
import random

BOT_TOKEN = ""
BOT_NAME = "math-bot"

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.command()
async def subtraction(ctx):
	global correct
	global current_question
	num1 = random.randint(0, 500)
	num2 = random.randint(0, num1)
	correct = str(num1 - num2)
	current_question = "subtract"
	await ctx.send(f"What is {num1} - {num2} respond with $answer [your answer]")

@bot.command()
async def addition(ctx):
	global correct
	global current_question
	num1 = random.randint(0, 500)
	num2 = random.randint(0, 500)
	correct = str(num1 + num2)
	current_question = "add"
	await ctx.send(f"What is {num1} + {num2} respond with $answer [your answer]")

@bot.command()
async def add(ctx, *nums):
	result = 0
	i = 0
	for i in nums:
		result = result + int(i)
	await ctx.send(f"Result: {result}")

@bot.command()
async def subtract(ctx, num1, num2):
	result = int(num1) - int(num2)
	await ctx.send(f"Result: {result}")

@bot.command()
async def answer(ctx, answer):
	global correct
	global current_question
	if current_question == "":
		await ctx.send("No current question!")
	else:
		if answer == correct:
			if current_question == "add":
				await ctx.send(f"THIS PERSON JUST DID ADDITION WOW THE ANSWER WAS {correct}!")
			elif current_question == "subtract":
				await ctx.send(f"THIS PERSON JUST DID SUBTRACTION WOW THE ANSWER WAS {correct}!")
			correct = ""
			current_question = ""
		else:
			await ctx.send("Incorrect answer!")


bot.run(BOT_TOKEN)
