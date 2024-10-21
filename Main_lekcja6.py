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


import os
print(os.listdir('images'))
@bot.command()
async def animal(ctx):
    animal_name = random.choice(os.listdir('images'))
    with open(f'images/{animal_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


print(os.listdir('plants'))
@bot.command()
async def plant(ctx):
    plant_name = random.choice(os.listdir('plants'))
    with open(f'plants/{plant_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


print(os.listdir('colors'))
@bot.command()
async def color(ctx):
    color_name = random.choice(os.listdir('colors'))
    with open(f'colors/{color_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


print(os.listdir('food'))
@bot.command()
async def food(ctx):
    food_name = random.choice(os.listdir('food'))
    with open(f'food/{food_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


print(os.listdir('things'))
@bot.command()
async def thing(ctx):
    thing_name = random.choice(os.listdir('things'))
    with open(f'things/{thing_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


import requests
def get_image_dog_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def dog(ctx):
    image_url = get_image_dog_url()
    await ctx.send(image_url)

def get_image_duck_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    image_url = get_image_duck_url()
    await ctx.send(image_url)


@bot.command()
async def random_smiles(ctx):
     emojis = [':laughing:',':weary:', ':poop:', ':lying_face:', ':jack_o_lantern:']
     await ctx.send(f'Twoja emotka: {random.choice(emojis)}')
     await ctx.send(emojis)


@bot.command()
async def translate(ctx, slowo):
    slowa = {
        'hello': 'witam',
        'poop': 'pupa',
        'cat': 'kot',
        'apple': 'jabłko'
    }
    for key in slowa.keys():
        if key == slowo:
            await ctx.send(f'Tłumaczenie słowa {slowo} to: {slowa[key]}')
            break

@bot.command()
async def rdd(ctx):
     emojis = [':jack_o_lantern:', ':dress:', ':athletic_shoe:', ':ring:']
     await ctx.send(f'Twoje rękodzieło to: {random.choice(emojis)}')
     await ctx.send(emojis)


@bot.command()
async def ooodpad(ctx, odpad):
    odpady = {
        'plastik': 'worek żółty, rozpad 1000 lat',
        'metal': 'worek żółty, rozpad 100 lat',
        'szkło': 'worek zielony, rozpad 2000 lat',
        'papierek': 'worek niebieski, rozpad 1 rok',
        'odpady zmieszane': 'worek czarny, rozpad od 100 do 1000 lat'

    }
    for key in odpady.keys():
        if key == odpad:
            await ctx.send(f'xxxxxxxx {odpad} to: {odpady[key]}')
            break



bot.run('xxxxxx')
