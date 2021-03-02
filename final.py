import discord
import os
from discord.ext import commands

# from keep_alive import keep_alive

client = commands.Bot(command_prefix='.')


@client.command()  # add command
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


@client.command()  # hello return
async def hello(ctx):
    await ctx.send("Hello there")


@client.command()  # clear command
async def clear(ctx, amount=10 ** 9):
    await ctx.channel.purge(limit=amount)


@client.event  # member join message
async def on_member_join(member):
    print(f'{member} has joined a server.')
    await client.process_commands(member)


@client.event  # member left message
async def on_member_remove(member):
    print(f'{member} has left a server.')
    await client.process_commands(member)


@client.event  # bad language check example
async def on_message(message):
    if '$slangs' in message.content:
        await message.channel.send('Pinging {} DO NOT USE THIS KIND OF LANGUAGE HERE'.format(message.author.mention))
    await client.process_commands(message)


@client.command()  # ping
async def ping(ctx, member: discord.Member):
    await ctx.send(f"PONG {member}")


# def clr(): os.system('clear') #clear console
# clr()

# keep_alive
client.run(os.getenv("TOKEN"))
