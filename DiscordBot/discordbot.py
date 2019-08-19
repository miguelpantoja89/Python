import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '')#You can type the prefix you want

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print(f'{member} se ha unido al servidor.')

@client.event
async def on_member_remove(member):
    print(f'{member} se ha ido servidor.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')
@client.command(aliases=['test','pregunta'])
async def _8ball(ctx, *, question):
    responses = ['Claro que si', 'La vida es genial', 'Eres la caña', 'Eres malo', 'Todo es posible' , 'Lo siento', 'Felicidades']
    await ctx.send(f'Pregunta:{question}\nRespuesta: {random.choice(responses)}')
client.run('your-token')
