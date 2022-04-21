import os
import discord
from discord.ext import commands
#import asyncio
#import json
#from discord.utils import get
#from discord.ext.commands import has_permissions, MissingPermissions
import random


bot = commands.Bot(command_prefix= '$', description="So far, just rock paper scissors.")



## Rock paper scissors
@bot.command(name="rps", description="Play rock paper scissors against the bot!", pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rps(ctx):    
    em1 = discord.Embed(title="Rock Paper Scissors", description="What do you pick?", color=discord.Color.blue())
    msg = await ctx.send(embed=em1)
    rock = "🪨"
    paper = "🧻"
    scissors = "✂️"
    options = ["🪨", "🧻", "✂️"]
    await msg.add_reaction(rock)
    await msg.add_reaction(paper)
    await msg.add_reaction(scissors)

    def check(reaction, user):
      return user == ctx.author and str(reaction.emoji) in options 
    reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)

    random_number = random.randint(0,2)
    computer_pick = options[random_number]

    emtie = discord.Embed(title="Rock Paper Scissors", description="It's a tie!", color=discord.Color.teal())
    emwin = discord.Embed(title="Rock Paper Scissors", description="You won!", color=discord.Color.green())
    emlose = discord.Embed(title="Rock Paper Scissors", description="You lost!", color=discord.Color.red())

    if str(reaction.emoji) == rock and computer_pick == options[0]:
      await ctx.send("You picked: " + rock + "\n" + "Computer picked: " + rock)
      await ctx.send(embed=emtie)
    elif str(reaction.emoji) == rock and computer_pick == options[1]:
      await ctx.send("You picked: " + rock + "\n" + "Computer picked: " + paper)
      await ctx.send(embed=emlose)
    elif str(reaction.emoji) == rock and computer_pick == options[2]:
      await ctx.send("You picked: " + rock + "\n" + "Computer picked: " + scissors)
      await ctx.send(embed=emwin)
    elif str(reaction.emoji) == paper and computer_pick == options[0]:
      await ctx.send("You picked: " + paper + "\n" + "Computer picked: " + rock)
      await ctx.send(embed=emwin)
    elif str(reaction.emoji) == paper and computer_pick == options[1]:
      await ctx.send("You picked: " + paper + "\n" + "Computer picked: " + paper)
      await ctx.send(embed=emtie)
    elif str(reaction.emoji) == paper and computer_pick == options[2]:
      await ctx.send("You picked: " + paper + "\n" + "Computer picked: " + scissors)
      await ctx.send(embed=emlose)
    elif str(reaction.emoji) == scissors and computer_pick == options[0]:
      await ctx.send("You picked: " + scissors + "\n" + "Computer picked: " + rock)
      await ctx.send(embed=emlose)
    elif str(reaction.emoji) == scissors and computer_pick == options[1]:
      await ctx.send("You picked: " + scissors + "\n" + "Computer picked: " + paper)
      await ctx.send(embed=emwin)
    elif str(reaction.emoji) == scissors and computer_pick == options[2]:
      await ctx.send("You picked: " + scissors + "\n" + "Computer picked: " + scissors)
      await ctx.send(embed=emtie)     
        
    
      

@rps.error
async def rps_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Command cooldown",description=f"You can use this command again in `{error.retry_after:.2f}s`.", color=discord.Color.red())
        await ctx.send(embed=em)



## CHECK IF BOT IS WORKING $ping
@bot.command(name="ping", description="Test if the bot is working")
@commands.cooldown(1, 30, commands.BucketType.user)
async def ping(ctx):
    await ctx.send("Pong")
@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Command cooldown",description=f"You can use this command again in `{error.retry_after:.2f}s`.", color=discord.Color.red())
        await ctx.send(embed=em)  
    
        
      
## CONFIRM THE BOT IS ON IN CONSOLE
@bot.event
async def on_ready():
  print('this is {0.user}'.format(bot))




bot.run(os.environ['TOKEN'])
