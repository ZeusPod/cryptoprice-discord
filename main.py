import threading
import discord
from discord import embeds
from discord.colour import Color
from discord.ext import commands
from discord.utils import async_all
from pycoingecko import CoinGeckoAPI
import json
import datetime
import time 
from threading import Timer




def getprice():
    cg = CoinGeckoAPI()
    coinsprice = cg.get_price(ids='bitcoin, ethereum, dogecoin, tron, chainlink, tether, basic-attention-token, ripple, cardano, uniswap, binancecoin, monero, polkadot, litecion, bitcoin-cash ', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true')
    print(coinsprice)
    #Save the data in a Json file 
    with open ('data.json' ,'w') as file:
        json.dump(coinsprice, file, indent = 3)

    #Load data from Json file
    coinsfile = open ('data.json', 'r') 
    jsondata = coinsfile.read()
    #parser
    obj = json.loads(jsondata)
    threading.Timer(10,getprice).start()


def printtest():
    precios = getprice()
    print(precios)
    threading.Timer(8,printtest)

imprime = printtest()


#Discord bot 

bot = commands.Bot(command_prefix='>')

#events
@bot.event
async def on_ready():
    print('Bot activo')

@bot.command()
async def comandos(ctx):
    embed = discord.Embed(title = f"{ctx.guild.name}", description="comandos para consultar las cotizaciones", timestamp=datetime.
    datetime.utcnow(), color=discord.Color.orange())
    embed.add_field(name="Consulta BTC", value=">preciobtc")
    embed.add_field(name="Consulta ETH", value=">precioeth")
    embed.add_field(name="Consulta DOG", value=">preciodoge")
    embed.add_field(name="Consulta TRX", value=">preciotrx")
    embed.add_field(name="Consulta Link", value=">preciochainlink")
    await ctx.send(embed=embed)

#command BTC price
@bot.command()
async def preciobtc(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #btc price from jason
       btc = obj['bitcoin']
       precioBtc = btc['usd']
       btcmktcap = btc['usd_market_cap']
       vol_hrs = btc['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del BTC {precioBtc}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.gold())
       embed.add_field(name="**Market cap**", value =btcmktcap)
       embed.add_field(name="**Vol last 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1547033579")
       await ctx.send(embed=embed)

#ethreum price
@bot.command()
async def precioeth(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #ethreum price from jason
       eth = obj['ethereum']
       ethprice = eth['usd']
       ethmktcap = eth['usd_market_cap']
       vol_hrs = eth['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del Ethereum {ethprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
       embed.add_field(name="**Market cap**", value =ethmktcap)
       embed.add_field(name="**Vol last 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/279/small/ethereum.png?1595348880")
       await ctx.send(embed=embed)

#dogecoin price 

@bot.command()
async def preciodoge(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #tron price from jason
       doge = obj['dogecoin']
       dogeprice = doge['usd']
       dogemktcap = doge['usd_market_cap']
       vol_hrs = doge['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del Dogecoin {dogeprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gold())
       embed.add_field(name="**Market cap**", value =dogemktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/5/small/dogecoin.png?1547792256")
       await ctx.send(embed=embed)

#tron price 

@bot.command()
async def preciotrx(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #btc price from jason
       trx = obj['tron']
       trxprice = trx['usd']
       trxmktcap = trx['usd_market_cap']
       vol_hrs = trx['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del TRX {trxprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
       embed.add_field(name="**Market cap**", value =trxmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/1094/small/tron-logo.png?1547035066")
       await ctx.send(embed=embed)

#precio Chainlink 

@bot.command()
async def preciochainlink(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #Chainlink price from jason
       link = obj['chainlink']
       linkprice = link['usd']
       linkmktcap = link['usd_market_cap']
       vol_hrs= link['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del Chainlink {linkprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value =linkmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/877/small/chainlink-new-logo.png?1547034700")
       await ctx.send(embed=embed)

#tether
@bot.command()
async def preciotether(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #theter price from jason
       tether = obj['tether']
       tetherprice = tether['usd']
       tethermktcap = tether['usd_market_cap']
       vol_hrs= tether['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Tether {tetherprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
       embed.add_field(name="**Market cap**", value =tethermktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/325/small/Tether-logo.png?1598003707")
       await ctx.send(embed=embed)


#Precio del Bat

@bot.command()
async def preciobat(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #bat price from jason
       bat= obj['basic-attention-token']
       batprice = bat['usd']
       batmktcap = bat['usd_market_cap']
       vol_hrs= bat['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del BAT  {batprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_red())
       embed.add_field(name="**Market cap**", value = batmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/677/small/basic-attention-token.png?1547034427")
       await ctx.send(embed=embed)


#Precio de ripple

@bot.command()
async def precioxrp(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #xrp price from jason
       xrp = obj['ripple']
       xrpprice = xrp['usd']
       xrpmktcap = xrp['usd_market_cap']
       vol_hrs= xrp['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del XRP {xrpprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = xrpmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/44/small/xrp-symbol-white-128.png?1605778731")
       await ctx.send(embed=embed)

#precio cardano

@bot.command()
async def preciocardano(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #xrp price from jason
       car = obj['cardano']
       cardanoprice = car['usd']
       cardanomktcap = car['usd_market_cap']
       vol_hrs= car['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Cardano {cardanoprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="**Market cap**", value = cardanomktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/975/small/cardano.png?1547034860")
       await ctx.send(embed=embed)


#precio uniswap

@bot.command()
async def preciouniswap(ctx):
       #read json file 
       coinsfile = open ('data.json', 'r') 
       jsondata = coinsfile.read()
       #parser
       obj = json.loads(jsondata)
       #uniswap price from json
       uni = obj['uniswap']
       uniswapprice = uni['usd']
       uniswapmktcap = uni['usd_market_cap']
       vol_hrs= uni['usd_24h_vol']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio de Uniswap {uniswapprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.DARK_VIVID_PINK())
       embed.add_field(name="**Market cap**", value = uniswapmktcap)
       embed.add_field(name="**Vol in 24hrs**", value =vol_hrs)
       embed.add_field(name="Font", value="Coingecko")
       embed.add_field(name="Developer", value="**Jose Morales**")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/12504/small/uniswap-uni.png?1600306604")
       await ctx.send(embed=embed)


bot.run('ODMxMTg2MjQ3OTI0ODQyNTI3.YHRkhA.jf-u-GFzImrYlD8o-yzF6IJD7sU')