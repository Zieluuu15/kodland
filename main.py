import discord
import random
from bot_logic import gen_emot, gen_pass, coin  # Importowanie funkcji bez argumentów

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('hej hej hej hej :)')

    if message.content.startswith('!smile'):
        await message.channel.send(':wink:, :heart:, :smile:')

    if message.content.startswith('!emotka'):
        await message.channel.send(gen_emot())
 
    if message.content.startswith('!moneta'):
        await message.channel.send(coin())

    if message.content.startswith('!pass'):
        pass_length = random.randint(5, 25)  # Generowanie długości hasła w tym miejscu
        generated_password = gen_pass(pass_length)
        await message.channel.send(generated_password)

# Uruchomienie klienta Discord

client.run('xxxxx')
