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
       vol_hrs = btc['usd_24h_change']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del BTC {precioBtc}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.gold())
       embed.add_field(name="Capitalizacion de mercado", value =btcmktcap)
       embed.add_field(name="Volumen en 24hrs", value =vol_hrs)
       embed.add_field(name="Fuente de precio", value="Powered by Coingecko")
       embed.add_field(name="Dev", value="Jose Morales")
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
       #btc price from jason
       eth = obj['ethereum']
       ethprice = eth['usd']
       ethmktcap = eth['usd_market_cap']
       vol_hrs = eth['usd_24h_change']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del Ethereum {ethprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
       embed.add_field(name="Capitalizacion de mercado", value =ethmktcap)
       embed.add_field(name="Volumen en 24hrs", value =vol_hrs)
       embed.add_field(name="Fuente de precio", value="Powered by Coingecko")
       embed.add_field(name="Dev", value="Jose Morales")
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
       #btc price from jason
       doge = obj['dogecoin']
       dogeprice = doge['usd']
       dogemktcap = doge['usd_market_cap']
       vol_hrs = doge['usd_24h_change']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del Dogecoin {dogeprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gold())
       embed.add_field(name="Capitalizacion de mercado", value =dogemktcap)
       embed.add_field(name="Volumen en 24hrs", value =vol_hrs)
       embed.add_field(name="Fuente de precio", value="Powered by Coingecko")
       embed.add_field(name="Dev", value="Jose Morales")
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
       embed.add_field(name="Capitalizacion de mercado", value =trxmktcap)
       embed.add_field(name="Volumen en 24hrs", value =vol_hrs)
       embed.add_field(name="Fuente de precio", value="Powered by Coingecko")
       embed.add_field(name="Dev", value="Jose Morales")
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
       #btc price from jason
       link = obj['chainlink']
       linkprice = link['usd']
       linkmktcap = link['usd_market_cap']
       vol_hrs= link['usd_24h_change']
       embed = discord.Embed(title = f"{ctx.guild.name}", description=f"**Precio del Chainlink {linkprice} $**", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
       embed.add_field(name="Capitalizacion de mercado", value =linkmktcap)
       embed.add_field(name="Volumen en 24hrs", value =vol_hrs)
       embed.add_field(name="Fuente de precio", value="Powered by Coingecko")
       embed.add_field(name="Dev", value="Jose Morales")
       embed.set_thumbnail(url="https://assets.coingecko.com/coins/images/877/small/chainlink-new-logo.png?1547034700")
       await ctx.send(embed=embed)








bot.run('ODMxMTg2MjQ3OTI0ODQyNTI3.YHRkhA.jf-u-GFzImrYlD8o-yzF6IJD7sU')