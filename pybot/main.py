import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
import logging

handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')

load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'online: {bot.user}')


@bot.command()
async def greet(ctx):
    await ctx.send(f"hey{ctx.author.mention}")


@bot.command()
async def msg(ctx, arg):
    await ctx.send(f"your message was{arg}")


new_role = "admin"


@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    print(role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"your role was succesfully added")
        return
    await ctx.send(f"role not found")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    print(role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"your role was succesfully removed")
        return
    await ctx.send(f"role not found")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "adolf" in message.content.lower():
        await message.delete()
        channel = message.channel
        await channel.send(f'Halt stop!')
    await bot.process_commands(message)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)