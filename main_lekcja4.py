import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!, {ctx.author.mention}')

@bot.command()
async def hej(ctx, count=5):
    await ctx.send('hej! '  * count)


import random
@bot.command()
async def password(ctx,length=10):
    symbols = '123456789!@#$%^&*-_=+;:.,<>/?`|'
    password = ''
    for i in range(length):
        password += random.choice(symbols)
    await ctx.send(f'Twoje hasło to: {password}')

@bot.command()
async def suma(ctx, a: int, b:int):
    await ctx.send(f'Suma {a} + {b} =  {a+b}')

@bot.command()
async def roz(ctx, a: int, b:int):
    await ctx.send(f'Suma {a} - {b} =  {a-b}')

@bot.command()
async def mno(ctx, a: int, b:int):
    await ctx.send(f'Suma {a} * {b} =  {a*b}')


@bot.command()
async def dziel(ctx, a: int, b:int):
    await ctx.send(f'Suma {a} / {b} =  {a/b}')

bot.run('xxxxx')
