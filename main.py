import discord
import os
import random
import requests
import time
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def ra_em():
    emoji = ["😀", "😋", "😭", "🎈", "✨", "🎮", "👻", "🐱‍👤"]
    return random.choice(emoji)

def ra_is():
    sekil = ["('‿')", "(★‿★)", "♪(´▽｀)", "(ツ)", "(⓿_⓿)", "(＞︿＜)"]
    return random.choice(sekil)
    
def flip_coin():
    flip = random.randint(1, 2)
    if flip == 1:
        return "YAZI"
    else:
        return "TURA"
    
def ra_sa():
    a = random.randint(0,100000)
    return a

def ra_re():
    renk = ["🔴","🟠","🟡","🟢","🔵","🟣","⚫"]
    return random.choice(renk)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba, benim adım {bot.user}! Ben bir botum!')

@bot.command()
async def yardım(ctx):
    await ctx.send(f"Komutlar: !hello !yardım !sayı !işaret !heh !topla !çıkar !çarp !böl !emoji !renk !elprimo !dynamike !edgar !mico !spike !para !mem !duck !dog")

@bot.command()
async def sayı(ctx):
    await ctx.send(ra_sa())

@bot.command()
async def üf(ctx):
    await ctx.send(f"Beynim yandığı için özür dilerim.")

@bot.command()
async def işaret(ctx):
    await ctx.send(ra_is())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx, toplanan_1 = 5, toplanan_2 = 5):
    await ctx.send(toplanan_1 + toplanan_2)

@bot.command()
async def çıkar(ctx, eksilen = 5, çıkan = 5):
    await ctx.send(eksilen - çıkan)

@bot.command()
async def çarp(ctx, çarpan_1 = 5, çarpan_2 = 5):
    await ctx.send(çarpan_1 * çarpan_2)

@bot.command()
async def böl(ctx, bölünen = 5, bölen = 5):
    await ctx.send(bölünen // bölen)

@bot.command()
async def emoji(ctx):
    await ctx.send(ra_em())

@bot.command()
async def gizli(ctx):
    await ctx.send(f"Vay canına bunu buldun...")
    time.sleep(2)
    await ctx.send(f"Ama nasıl?")
    time.sleep(2)
    await ctx.send(f"Madem bunu buldun o zaman birkaç bilgiyi hakettin")
    time.sleep(2)
    await ctx.send(f"Bot'un yapılma tarihi: 25.05.2024")
    await ctx.send(f"Yapan kişi: Atlas Sevdirir")
    await ctx.send(f"Atlas'a nasıl ulaşırım: Discord: camuka2.0 / E-posta: sevdirira@gmail.com")
    await ctx.send(f"Not: Bir gizli komut daha var.")

@bot.command()
async def renk(ctx):
    await ctx.send(ra_re())

@bot.command()
async def XCFDGA548P(ctx):
    await ctx.send(f"Bunu bulmak zor olmadı değil mi? Seni HİLE!")
    await ctx.send(f"@Admin yok et bu kullanıcıyı!")

@bot.command()
async def para(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

    
@bot.command()
async def elprimo(ctx):
    resimler_listesi = os.listdir('krk_images') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'krk_images/{"elprimo.png"}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
        await ctx.send(f"Bu Brawl Stars'tan El Primo! Can = 12000 / Hız = Hızlı / Hasar = 3040")
        await ctx.send(file=picture)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!

@bot.command()
async def dynamike(ctx):
    resimler_listesi = os.listdir('krk_images') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'krk_images/{"dynamike.png"}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
        await ctx.send(f"Bu Brawl Stars'tan Dynamike! Can = 5600 / Hız = Hızlı / Hasar = 3200")
        await ctx.send(file=picture)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!

@bot.command()
async def edgar(ctx):
    resimler_listesi = os.listdir('krk_images') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'krk_images/{"edgar.png"}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
        await ctx.send(f"Bu Brawl Stars'tan Edgar! Can = 6600 / Hız = Çok Hızlı / Hasar = 2160")
        await ctx.send(file=picture)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!

@bot.command()
async def mico(ctx):
    resimler_listesi = os.listdir('krk_images') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'krk_images/{"mico.png"}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
        await ctx.send(f"Bu Brawl Stars'tan Mico! Can = 6000 / Hız = Çok Hızlı / Hasar = 2180")
        await ctx.send(file=picture)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!

@bot.command()
async def spike(ctx):
    resimler_listesi = os.listdir('krk_images') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'krk_images/{"spike.png"}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
        await ctx.send(f"Bu Brawl Stars'tan Spike! Can = 4800 / Hız = Normal / Hasar = 3240")
        await ctx.send(file=picture)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    

@bot.command()
async def mem(ctx):
    resimler_listesi = os.listdir('images') #['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg']
    with open(f'images/{random.choice(resimler_listesi)}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("TOKEN")