import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def animals(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)

sampah_organik = ['daun','kertas','sisa makanan'] 
sampah_anorganik = ['plastik','kaleng','kabel'] 

@bot.command()
async def pilih_sampah(ctx):
      await ctx.send('masukkan jenis sampah: ')
      msg = await bot.wait_for('message')
      if msg.content in sampah_organik: 
            await ctx.send('masukkan sampah organik')
      if msg.content in sampah_anorganik: 
            await ctx.send('masukkan sampah anorganik')      

bot.run("masukkan token")
